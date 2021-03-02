import boot

boot.run("matmul_run_000", "matmul_run", ((512, 4608), (4608, 4608), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), ([12, 12], [8, 8], [16, 16], [16, 16], [4, 2]))
boot.run("matmul_run_001", "matmul_run", ((256, 2304), (2304, 2304), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), ([6, 6], [4, 4], [16, 16], [16, 16], [9, 9]))
boot.run("matmul_run_002", "matmul_run", ((512, 512), (512, 4608), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), ([36, 12], [2, 2], [16, 16], [16, 16], [32, 4]))
boot.run("matmul_run_003", "matmul_run", ((2048, 2048), (2048, 512), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"),([8, 8], [4, 4], [16, 16], [16, 16], [128, 8]))
boot.run("matmul_run_004", "matmul_run", ((256, 1024), (1024, 1024), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"),([8, 8], [8, 8], [16, 16], [16, 16], [4, 1]))
boot.run("matmul_run_005", "matmul_run", ((1024, 256), (256, 256), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"), ([4, 4], [16, 4], [16, 16], [16, 16], [16, 8]))
boot.run("matmul_run_006", "matmul_run", ((1024, 1024), (1024, 256), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"),([2, 1], [4, 2], [16, 16], [16, 16], [64, 64]))
boot.run("matmul_run_007", "matmul_run", ((128, 1152), (1152, 1152), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"),([9, 9], [8, 8], [16, 16], [16, 16], [18, 1]))
boot.run("matmul_run_008", "matmul_run", ((256, 256), (256, 2304), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"),([12, 12], [4, 4], [16, 16], [16, 16], [2, 1]))
boot.run("matmul_run_009", "matmul_run", ((512, 2048), (2048, 2048), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"),([32, 32], [4, 4], [16, 16], [16, 16], [4, 4]))
boot.run("matmul_run_010", "matmul_run", ((2048, 2048), (2048, 1024), 0, 'zN', 'zN', 'zN', False, False, 'float16', None, 'float32', "matmul"),([8, 8], [4, 4], [16, 16], [16, 16], [8, 8]))