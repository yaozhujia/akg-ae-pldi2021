import boot

boot.run("matmul_run_041", "matmul_run",((512, 256), (256, 256), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[4, 2], [8, 4], [16, 16], [16, 16], [16, 16]])
boot.run("matmul_run_042", "matmul_run",((1024, 512), (512, 512), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"),[[4, 4], [1, 1], [16, 16], [16, 16], [32, 32]])
boot.run("matmul_run_043", "matmul_run",((256, 256), (256, 512), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[8, 8], [8, 4], [16, 16], [16, 16], [16, 4]])
boot.run("matmul_run_044", "matmul_run",((64, 256), (256, 256), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[4, 4], [4, 4], [16, 16], [16, 16], [8, 2]])
boot.run("matmul_run_045", "matmul_run",((64, 784), (784, 784), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[7, 7], [4, 4], [16, 16], [16, 16], [7, 7]])
boot.run("matmul_run_046", "matmul_run",((64, 64), (64, 256), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[2, 2], [4, 4], [16, 16], [16, 16], [4, 2]])
boot.run("matmul_run_047", "matmul_run",((128, 256), (256, 256), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[4, 4], [8, 8], [16, 16], [16, 16], [4, 2]])
boot.run("matmul_run_048", "matmul_run",((64, 64), (64, 64), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[4, 4], [4, 4], [16, 16], [16, 16], [2, 1]])
boot.run("matmul_run_049", "matmul_run",((128, 128), (128, 256), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[8, 8], [8, 8], [16, 16], [16, 16], [4, 1]])
boot.run("matmul_run_050", "matmul_run",((64, 64), (64, 784), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), [[7, 7], [4, 4], [16, 16], [16, 16], [4, 1]])

