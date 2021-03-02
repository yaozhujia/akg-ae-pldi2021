# Copyright 2020-2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os
import json
import pytest
import logging
from akg import composite
from akg.utils import custom_tiling
from akg.utils import kernel_exec as utils
from akg.utils.result_analysis import gpu_profiling
from akg.utils.format_transform import to_tvm_nd_array
from gen_json_data import gen_json_data
from base import get_rtol_atol
from tensorio import compare_tensor

logging.getLogger().setLevel(logging.INFO)


def print_usage():
    logging.info("\nUsage:")
    logging.info("1. To run single file :")
    logging.info(
        "  python test_composite_json.py [-c, -a/--auto] -f <filename>.")
    logging.info("2. To run files in a directory, default to be ./json_dir :")
    logging.info("  python test_composite_json.py -d [-a or --auto]")
    logging.info("3. To run ci files :")
    logging.info("  python test_composite_json.py --ci [-a/--auto, --profile]")
    logging.info("\nOptions:")
    logging.info("-f <filename>")
    logging.info("  single file name, '*.info' or '*.json'.")
    logging.info("-c")
    logging.info("  use tiling dim attribute.")
    logging.info("-a, --auto")
    logging.info("  use poly schedule mode.")
    logging.info("--profile")
    logging.info("  use profiling env.")
    logging.info("\n")


def get_result(desc, poly, attrs=None):
    if poly:
        reduce_lib_key = "enable_akg_reduce_lib"
        if reduce_lib_key not in attrs.keys():
            attrs[reduce_lib_key] = poly
    if attrs == {}:
        mod = composite.build(desc, poly=poly)
    else:
        mod = composite.build(desc, attrs, poly=poly)
    input_for_mod, expect, output_indexes = gen_json_data(desc)
    output = utils.mod_launch(mod, input_for_mod, output_indexes)

    rtol, atol = get_rtol_atol("FUSED", "float32")
    flag = True
    if len(output_indexes) > 1:
        if not all(map(lambda x, y: compare_tensor(x, y, rtol=rtol, atol=atol), output, expect)):
            logging.info(mod.imported_modules[0].get_source())
            flag = False
    else:
        if not compare_tensor(output, expect, rtol=rtol, atol=atol):
            logging.info(mod.imported_modules[0].get_source())
            flag = False
    desc_d = json.loads(desc)
    if desc_d["process"] == "cuda":
        inputs = to_tvm_nd_array(input_for_mod)
        expect = to_tvm_nd_array(expect)
        gpu_profiling(mod, *inputs, *expect, repeat_time=400)
    return flag


def _should_use_poly(kernel_info):
    """Judge whether to use poly."""
    if os.getenv('MS_AKG_USE_POLY') == "on":
        return True
    for desc in kernel_info['op_desc']:
        if desc['name'].startswith('Reduce'):
            return True
    return False


def _enable_atomic_add(kernel_info):
    """Judge whether to enable atomic add."""
    for op in kernel_info["op_desc"]:
        if not op["attr"]:
            continue
        for attr in op["attr"]:
            if attr["name"] == "enable_atomic_add" and attr["value"]:
                return True
    return False


def _add_composite_attrs(desc, attrs, poly=True):
    if isinstance(desc, str):
        json_obj = json.loads(desc)
    elif isinstance(desc, dict):
        json_obj = desc
    else:
        return poly

    if not poly:
        return False
    use_poly = _should_use_poly(json_obj)
    if use_poly and _enable_atomic_add(json_obj):
        attrs["enable_atomic_add"] = True
    return use_poly


@pytest.mark.skip
def test_single_file(input_file, use_custom, poly=False):
    with open(input_file, 'r') as f:
        desc = f.read()
        attrs = {}
        if use_custom:
            attrs["dim"] = custom_tiling.set_dims(((4, 1), (4, 1)))
        use_poly = _add_composite_attrs(desc, attrs, poly)
        flag = get_result(desc, use_poly, attrs)
        if flag:
            logging.info("Run Pass!")
        else:
            logging.info("Precision Error")


@pytest.mark.level0
@pytest.mark.platform_gpu
def test_json_dir(poly=False):
    json_dir = "./json_dir/"
    json_dims_file = "./json_dir/dims.json"
    files = os.listdir(json_dir)
    flag = True
    with open(json_dims_file, 'r') as f:
        base = f.read()
        dims_dict = json.loads(base)
    idx = 1
    for input_file in files:
        with open(json_dir + input_file, 'r') as f:
            if input_file == "dims.json":
                continue
            logging.info("Begin run No.%d file:%s" % (idx, input_file))
            idx = idx + 1
            desc = f.read()
            attrs = {}
            if input_file in dims_dict:
                dim_info = dims_dict[input_file]
                attrs = {'dim': dim_info}
            use_poly = _add_composite_attrs(desc, attrs, poly)
            flag = get_result(desc, use_poly, attrs)
            if not flag:
                logging.info("----------Error Json name is----------")
                logging.info(input_file)
                raise ValueError("Precision Error")
    logging.info("All Json files run PASS!")


def get_op_cycles_info(desc, cycle_info_file, old_op_cycles=100000000):
    with open(cycle_info_file, 'r') as f:
        op_cycles = int(f.read())
    diff = old_op_cycles - op_cycles
    return op_cycles, diff


@pytest.mark.level0
@pytest.mark.platform_gpu
def test_ci(profile=False, poly=False):
    ci_path = "./need_adapt/"
    if profile:
        need_update = False
        base_json_file = "./need_adapt/base.json"
        cycle_info_file = "./cycle_path/a.txt"
        os.environ['PROFILING'] = "true"
        os.environ['CYCLES_PATH'] = os.getcwd() + '/' + cycle_info_file
        with open(base_json_file, 'r') as f:
            base = f.read()
            old_dict = json.loads(base)
    files = os.listdir(ci_path)
    for fi in files:
        with open(ci_path + fi, 'r') as f:
            if fi == "base.json":
                continue
            desc = f.read()
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  fi: ", fi)
            flag = get_result(desc, poly)
            if not flag:
                logging.info("----------Error Json info is----------")
                logging.info(desc)
                raise ValueError("Precision Error")
            elif not profile:
                logging.info("Composite Json {} pass!".format(fi))
            else:
                old_op_cycles = old_dict[fi]
                op_cycles, diff = get_op_cycles_info(
                    desc, cycle_info_file, old_op_cycles)
                logging.info("~~~~~~~~~~~cycle diff is~~~~~~~~~~~")
                logging.info(diff)
                if diff > 500:
                    need_update = True
                    logging.info("Find Better Cycle the Json Info is:")
                    logging.info(desc)
                    logging.info("The Better Cycle is:")
                    logging.info(op_cycles)
                    old_dict[fi] = op_cycles
                elif diff < -1000:
                    logging.info("----------Error Json info is----------")
                    logging.info(desc)
                    raise ValueError("Performance Degradation")
            assert(flag)
    logging.info("All ops are ok!")
    if profile:
        if need_update:
            logging.info("Need to Update Baseline!!!")
            with open(base_json_file, 'w', encoding='utf-8') as f:
                json.dump(old_dict, f, indent=4)
        else:
            logging.info(
                "No significant performance improvement. Do not need to update Baseline!")


def main(argv):
    import getopt
    try:
        options, args = getopt.getopt(argv, "adcf:", ["auto", "ci", "profile"])
        poly = False
        use_custom = False
        single_file = False
        dir_test = False
        ci_test = False
        use_profiling = False
        for option, value in options:
            if option in ("-a", "--auto"):
                poly = True
            elif option == "-d":
                dir_test = True
            elif option == "-c":
                use_custom = True
            elif option == "-f":
                single_file = True
                file_name = value
            elif option == "--profile":
                use_profiling = True
    except:
        print_usage()
        return

    if single_file and (file_name.endswith(".info") or file_name.endswith(".json")):
        test_single_file(file_name, use_custom, poly)
    elif dir_test:
        test_json_dir(poly)
    elif ci_test:
        test_ci(use_profiling, poly)
    else:
        print_usage()


if __name__ == "__main__":
    main(sys.argv[1:])
