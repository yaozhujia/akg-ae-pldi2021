import boot
# test case for op8
boot.run("op8_000", "add_run", ([16, 128, 7, 7, 16], [16, 128, 7, 7, 16], "float32", "add_fp32"))
boot.run("op8_001", "add_run", ([16, 16, 56, 56, 16], [16, 16, 56, 56, 16], "float32", "add_fp32"))
boot.run("op8_002", "add_run", ([16, 32, 28, 28, 16], [16, 32, 28, 28, 16], "float32", "add_fp32"))
boot.run("op8_003", "add_run", ([16, 64, 14, 14, 16], [16, 64, 14, 14, 16], "float32", "add_fp32"))
boot.run("op8_004", "add_run", ([16, 128, 7, 7, 16], [16, 128, 7, 7, 16], "float16", "add_fp16"))
boot.run("op8_005", "add_run", ([16, 16, 56, 56, 16], [16, 16, 56, 56, 16], "float16", "add_fp16"))
boot.run("op8_006", "add_run", ([16, 32, 28, 28, 16], [16, 32, 28, 28, 16], "float16", "add_fp16"))
boot.run("op8_007", "add_run", ([16, 64, 14, 14, 16], [16, 64, 14, 14, 16], "float16", "add_fp16"))
boot.run("op8_008", "add_run", ([16, 4, 56, 56, 16], [16, 4, 56, 56, 16], "float16", "add_fp16"))
boot.run("op8_009", "add_run", ([16, 4, 56, 56, 16], [16, 4, 56, 56, 16], "float32", "add_fp32"))