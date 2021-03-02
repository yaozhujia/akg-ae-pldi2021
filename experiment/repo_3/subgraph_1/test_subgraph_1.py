# This is the the test case of Table 1 and Figure 12.
import boot
boot.run("subgraph_1", "softmax_run", ((16, 16, 512, 512), "float16", -1, "softmax_fp16"))