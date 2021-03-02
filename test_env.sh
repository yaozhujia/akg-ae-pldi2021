pip_show_str=`pip3 show akg`
str1=${pip_show_str#*Location:}
str2=${str1%Requires*}
str3=${str2%?}
AKG_ROOT=${str3#* }
TVM_ROOT="${AKG_ROOT}/third_party/incubator-tvm"
LIBAKG_ROOT="${AKG_ROOT}/build"
export LD_LIBRARY_PATH=${LIBAKG_ROOT}:${LD_LIBRARY_PATH}
export PYTHONPATH=${TVM_ROOT}/python:${TVM_ROOT}/topi:${TVM_ROOT}/topi/python:${AKG_ROOT}/tests/common:${AKG_ROOT}/python:${AKG_ROOT}/tests/fuzz/tune:${PYTHONPATH}

export RUNTIME_MODE=air_cloud
export PROFILING=true

