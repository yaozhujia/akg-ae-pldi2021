import boot
# test case for op6
boot.run("op6_0001", "transpose_run", ((10240, 768), (0, 1,), "float32"))
boot.run("op6_0002", "transpose_run", ((1024, 12, 128, 128), (2, 0, 1, 3), "float32"))
boot.run("op6_0003", "transpose_run", ((1024, 12, 128, 64), (0, 2, 1, 3), "float32"))
boot.run("op6_0004", "transpose_run", ((1024, 12, 128, 64), (2, 0, 1, 3), "float32"))
boot.run("op6_0005", "transpose_run", ((1024, 128, 12, 64), (0, 2, 1, 3), "float32"))
boot.run("op6_0006", "transpose_run", ((1024, 768), (0, 1,), "float32"))
boot.run("op6_0007", "transpose_run", ((1, 12, 128, 128), (2, 0, 1, 3),"float32"))
boot.run("op6_0008", "transpose_run", ((1, 12, 128, 64), (0, 2, 1, 3), "float32"))
boot.run("op6_0009", "transpose_run", ((1, 12, 128, 64), (2, 0, 1, 3), "float32"))
boot.run("op6_0010", "transpose_run", ((1, 128, 12, 64), (0, 2, 1, 3), "float32"))