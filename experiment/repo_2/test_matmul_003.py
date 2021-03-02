import boot

boot.run("matmul_run_031", "matmul_run",((256, 256), (256, 64), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"),[[4, 4], [8, 8], [16, 16], [16, 16], [4, 1]])
boot.run("matmul_run_032", "matmul_run",((64, 576), (576, 576), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[3, 3], [2, 2], [16, 16], [16, 16], [6, 6]])
boot.run("matmul_run_033", "matmul_run",((128, 128), (128, 512), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[8, 4], [8, 4], [16, 16], [16, 16], [8, 2]])
boot.run("matmul_run_034", "matmul_run",((256, 64), (64, 64), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[2, 2], [8, 2], [16, 16], [16, 16], [4, 1]])
boot.run("matmul_run_035", "matmul_run",((512, 512), (512, 1024), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[16, 16], [8, 8], [16, 16], [16, 16], [2, 1]])
boot.run("matmul_run_036", "matmul_run",((256, 512), (512, 512), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[8, 1], [8, 4], [16, 16], [16, 16], [32, 8]])
boot.run("matmul_run_037", "matmul_run",((512, 512), (512, 256), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[8, 8], [8, 2], [16, 16], [16, 16], [32, 16]])
boot.run("matmul_run_038", "matmul_run",((1024, 1024), (1024, 512), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"),[[8, 8], [8, 8], [16, 16], [16, 16], [64, 8]])
boot.run("matmul_run_039", "matmul_run",((512, 1024), (1024, 1024), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[16, 16], [8, 8], [16, 16], [16, 16], [2, 1]])
boot.run("matmul_run_040", "matmul_run",((64, 64), (64, 576), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[3, 3], [4, 4], [16, 16], [16, 16], [1, 1]])