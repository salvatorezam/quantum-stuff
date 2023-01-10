import numpy as np

alpha = 2
beta = 2
delta = 1

total_comb = 2 ** (alpha + beta + delta)

C = np.zeros((total_comb, total_comb))

for S in range(0, total_comb):
    S_1 = S >> (alpha - 1)
    S_2 = S_1 >> (beta - 1)
    S_3 = S_2 >> (alpha - 1)
    # S_4 = S_3 >>
    print(S_1)
