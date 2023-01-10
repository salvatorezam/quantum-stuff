# importing Qiskit
from qiskit import (
    Aer,
    transpile,
    QuantumCircuit,
    ClassicalRegister,
    QuantumRegister,
)

from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

import math


def main():

    coin = QuantumRegister(1, name="coin")
    mbit = ClassicalRegister(1, name="m")

    qc = QuantumCircuit(coin, mbit)

    qc.ry(3 * math.pi / 4, 0)

    qc.measure(coin, mbit)

    # --------------------- AER SIMULATION --------------------------------
    aer_sim = Aer.get_backend("aer_simulator")
    transpiled_qc = transpile(qc, aer_sim)
    result = aer_sim.run(transpiled_qc).result()
    plot_histogram(result.get_counts())
    plt.show()


if __name__ == "__main__":
    main()
