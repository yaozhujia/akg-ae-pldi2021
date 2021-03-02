import boot

# test case for op9 and op10
boot.run("op_9_10_000", "bn_split_run", ((16, 128, 7, 7, 16), "float32", 0.1, 1e-4, "resnet50_bn_split_000"))
boot.run("op_9_10_001", "bn_split_run", ((16, 16, 14, 14, 16), "float32", 0.1, 1e-4, "resnet50_bn_split_001"))
boot.run("op_9_10_002", "bn_split_run", ((16, 16, 56, 56, 16), "float32", 0.1, 1e-4, "resnet50_bn_split_002"))
boot.run("op_9_10_003", "bn_split_run", ((16, 32, 28, 28, 16), "float32", 0.1, 1e-4, "resnet50_bn_split_003"))
boot.run("op_9_10_004", "bn_split_run", ((16, 32, 7, 7, 16), "float32", 0.1, 1e-4, "resnet50_bn_split_004"))
boot.run("op_9_10_005", "bn_split_run", ((16, 4, 112, 112, 16), "float32", 0.1, 1e-4, "resnet50_bn_split_005"))
boot.run("op_9_10_006", "bn_split_run", ((16, 4, 56, 56, 16), "float32", 0.1, 1e-4, "resnet50_bn_split_006"))
boot.run("op_9_10_007", "bn_split_run", ((16, 64, 14, 14, 16), "float32", 0.1, 1e-4, "resnet50_bn_split_007"))
boot.run("op_9_10_008", "bn_split_run", ((16, 8, 28, 28, 16), "float32", 0.1, 1e-4, "resnet50_bn_split_008"))
boot.run("op_9_10_009", "bn_split_run", ((16, 8, 56, 56, 16), "float32", 0.1, 1e-4, "resnet50_bn_split_009"))
boot.run("op_9_10_010", "bn_split_run", ((16, 16, 28, 28, 16), "float32", 0.1, 1e-4, "resnet50_bn_split_010"))
boot.run("op_9_10_011", "bn_split_run", ((16, 32, 14, 14, 16), "float32", 0.1, 1e-4, "resnet50_bn_split_011"))