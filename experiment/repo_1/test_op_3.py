import boot

# test case for op3
boot.run("op3_000", "relu_run", ((16, 128, 7, 7, 16), "float32", 1e-5))
boot.run("op3_001", "relu_run", ((16, 16, 14, 14, 16), "float32", 1e-5))
boot.run("op3_002", "relu_run", ((16, 16, 56, 56, 16), "float32", 1e-5))
boot.run("op3_003", "relu_run", ((16, 32, 28, 28, 16), "float32", 1e-5))
boot.run("op3_004", "relu_run", ((16, 32, 7, 7, 16), "float32", 1e-5))
boot.run("op3_005", "relu_run", ((16, 4, 112, 112, 16), "float32", 1e-5))
boot.run("op3_006", "relu_run", ((16, 4, 56, 56, 16), "float32", 1e-5))
boot.run("op3_007", "relu_run", ((16, 64, 14, 14, 16), "float32", 1e-5))
boot.run("op3_008", "relu_run", ((16, 8, 28, 28, 16), "float32", 1e-5))
boot.run("op3_009", "relu_run", ((16, 8, 56, 56, 16), "float32", 1e-5))