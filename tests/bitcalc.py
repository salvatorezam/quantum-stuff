import matplotlib.pyplot as plt
import numpy as np


# # -- qubits as a funciton of dimention of grid --
# dim = 11

# dimensions = np.array([i for i in (2 ** p for p in range(1, 11))])

# qea_bits = np.array(
#     [
#         10 * n ** 2 - 6 * n + np.ceil(np.log2(n ** 2)) - 4
#         for n in (2 ** p for p in range(1, dim))
#     ]
# )
# new_bits = np.array(
#     [
#         2 * n ** 2 + 6 * n + np.ceil(np.log2(n ** 2)) - 4
#         for n in (2 ** p for p in range(1, dim))
#     ]
# )


# print(dimensions)
# print(qea_bits)
# print(new_bits)

# plt.plot(dimensions, qea_bits, marker="o")
# plt.plot(dimensions, new_bits, marker="o")

# plt.xlabel("dimension of grid")
# plt.ylabel("qubits")

# plt.show()

# -- qubits as a function of steps of 4x4 --
n = 4
max_steps = 2 * n - 2

steps_label = np.array([i for i in range(1, max_steps + 1)])

qea_bits = np.array(
    [
        np.ceil(np.log2(n ** 2)) + 2 * i + 4 * n + n * i - 5
        for i in range(1, max_steps + 1)
    ]
)


print(steps_label)
print(qea_bits)

plt.plot(steps_label, qea_bits, marker="o")

plt.xlabel("steps")
plt.ylabel("qubits")

plt.show()

# max_dim = 10

# dims = np.array([i for i in range(2, max_dim + 1)])
# qubits = np.array(
#     [np.ceil(np.log2(n ** 2)) * (2 * n - 1) + 2 * (2 * n - 2) + 2 for n in dims]
# )

# print(dims)
# print(qubits)

# plt.plot(dims, qubits, marker="o")
# plt.xlabel("dimension of grid")
# plt.ylabel("qubits")
# plt.show()


# for m in range(2, 11):
#     # grid_index = m ** 2 - 1
#     bits = (2 + np.ceil(np.log2(m - 1))) * (2 * m - 2)
#     print(f"Dim {m}: {int(bits)}")
