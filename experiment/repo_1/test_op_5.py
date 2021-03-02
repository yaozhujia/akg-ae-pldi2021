import boot

# test case for op5
boot.run("op5_000", "cast_run", ((16, 128, 16, 16), "float32", "float16"))
boot.run("op5_001", "cast_run", ((16, 64, 16, 16), "float32", "float16"))
boot.run("op5_002", "cast_run", ((16, 32, 16, 16), "float32", "float16"))
boot.run("op5_003", "cast_run", ((16, 16, 16, 16), "float32", "float16"))
boot.run("op5_004", "cast_run", ((16, 4, 16, 16), "float32", "float16"))
boot.run("op5_005", "cast_run", ((16, 4, 112, 112, 16), "float16", "float32"))
boot.run("op5_006", "cast_run", ((16, 4, 56, 56, 16), "float32", "float16"))
boot.run("op5_007", "cast_run", ((16, 16, 56, 56, 16), "float16", "float32"))
boot.run("op5_008", "cast_run", ((16, 4, 16, 16), "float32", "float16"))
boot.run("op5_009", "cast_run", ((16, 4, 16, 16), "float32", "float16"))