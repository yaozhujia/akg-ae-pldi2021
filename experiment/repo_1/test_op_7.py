import boot
# test case for op7
boot.run("op7_001", "one_hot_run", ((128,), 2, "int32", 1, 0, -1))
boot.run("op7_002", "one_hot_run", ((160,), 21128, "int32", 1, 0, -1))
boot.run("op7_003", "one_hot_run", ((16,), 2, "int32", 1, 0, -1))
boot.run("op7_004", "one_hot_run", ((20,), 21128, "int32", 1, 0, -1))
boot.run("op7_005", "one_hot_run", ((2,), 2, "int32", 1, 0, -1))
boot.run("op7_006", "one_hot_run", ((2560,), 21128, "int32", 1, 0, -1))
boot.run("op7_007", "one_hot_run", ((1,), 2, "int32", 1, 0, -1))
boot.run("op7_008", "one_hot_run", ((320,), 21128, "int32", 1, 0, -1))
boot.run("op7_009", "one_hot_run", ((32,), 2, "int32", 1, 0, -1))
boot.run("op7_010", "one_hot_run", ((40,), 21128, "int32", 1, 0, -1))