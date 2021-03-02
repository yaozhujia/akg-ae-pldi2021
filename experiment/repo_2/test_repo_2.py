# This is the all the test case of GEMM product in Figure 11.
import boot
boot.run("matmul_run_bert_001", "matmul_run", ((1008, 1008), (1008, 2048), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_002", "matmul_run", ((1008, 2048), (2048, 2048), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_003", "matmul_run", ((2048, 2048), (2048, 512), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_004", "matmul_run", ((2048, 512), (512, 512), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_005", "matmul_run", ((512, 512), (512, 4608), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_006", "matmul_run", ((512, 4608), (4608, 4608), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_007", "matmul_run", ((512, 512), (512, 2048), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_008", "matmul_run", ((512, 2048), (2048, 2048), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_009", "matmul_run", ((2048, 2048), (2048, 1024), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0010", "matmul_run", ((2048, 1024), (1024, 1024), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0011", "matmul_run", ((512, 512), (512, 1024), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0012", "matmul_run", ((512, 1024), (1024, 1024), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0013", "matmul_run", ((1024, 1024), (1024, 256), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0014", "matmul_run", ((1024, 256), (256, 256), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0015", "matmul_run", ((256, 256), (256, 2304), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0016", "matmul_run", ((256, 2304), (2304, 2304), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0017", "matmul_run", ((256, 256), (256, 1024), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0018", "matmul_run", ((256, 1024), (1024, 1024), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0019", "matmul_run", ((1024, 1024), (1024, 512), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0020", "matmul_run", ((1024, 512), (512, 512), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0021", "matmul_run", ((256, 256), (256, 512), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0022", "matmul_run", ((256, 512), (512, 512), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0023", "matmul_run", ((512, 512), (512, 128), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0024", "matmul_run", ((512, 128), (128, 128), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0025", "matmul_run", ((128, 128), (128, 1152), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0026", "matmul_run", ((128, 1152), (1152, 1152), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0027", "matmul_run", ((128, 128), (128, 1152), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0028", "matmul_run", ((128, 512), (512, 512), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0029", "matmul_run", ((512, 512), (512, 256), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0030", "matmul_run", ((512, 256), (256, 256), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0031", "matmul_run", ((128, 128), (128, 256), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0032", "matmul_run", ((128, 256), (256, 256), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0033", "matmul_run", ((256, 256), (256, 64), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0034", "matmul_run", ((256, 64), (64, 64), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0035", "matmul_run", ((64, 64), (64, 576), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0036", "matmul_run", ((64, 576), (576, 576), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0037", "matmul_run", ((64, 64), (64, 256), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0038", "matmul_run", ((64, 256), (256, 256), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0039", "matmul_run", ((64, 64), (64, 64), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0040", "matmul_run", ((64, 64), (64, 784), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
boot.run("matmul_run_bert_0041", "matmul_run", ((64, 784), (784, 784), 0, "zN", "zN", "zN", False, False, "float16", None, "float32", "matmul_cce"))
