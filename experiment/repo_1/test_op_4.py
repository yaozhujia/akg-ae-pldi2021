import boot

# test case for op4
boot.run("op4_000", "batchmatmul_run", ((), 16, 10, 2048, (10,), "float32", False, True, "output"))
boot.run("op4_001", "batchmatmul_run", ((), 2048, 10, 16, (), "float32", True, False, "output"))
boot.run("op4_002", "batchmatmul_run", ((), 16, 2048, 10, (), "float32", False, False, "output"))
boot.run("op4_003", "batchmatmul_run", ((), 2048, 1001, 16, (), "float32", True, False, "output"))
boot.run("op4_004", "batchmatmul_run", ((), 16, 2048, 1001, (), "float32", False, False, "output"))
boot.run("op4_005", "batchmatmul_run", ((), 16, 1001, 2048, (1001,), "float32", False, True, "output"))
boot.run("op4_006", "batchmatmul_run", ((), 16, 10, 2048, (10,), "float16", False, True, "output"))
boot.run("op4_007", "batchmatmul_run", ((), 16, 2048, 10, (), "float16", False, False, "output"))
boot.run("op4_008", "batchmatmul_run", ((), 2048, 1001, 16, (), "float16", True, False, "output"))
boot.run("op4_009", "batchmatmul_run", ((), 1001, 2048, 16, (), "float32", True, False, "output"))