from qiskit import IBMQ, transpile
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

from qiskit.tools.monitor import job_monitor
from qiskit.providers.ibmq import least_busy

from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


def main():

    coin = QuantumRegister(1, name="coin")
    mbit = ClassicalRegister(1, name="m")

    qc = QuantumCircuit(coin, mbit)

    for _ in range(200):
        qc.h(coin)
        qc.barrier()

    qc.measure(coin, mbit)

    provider = IBMQ.load_account()
    provider = IBMQ.get_provider("ibm-q")
    backend = least_busy(
        provider.backends(
            filters=lambda x: x.configuration().n_qubits >= 3
            and not x.configuration().simulator
            and x.status().operational == True
        )
    )
    print(f"Least busy backend: {backend}")

    print(f" -- Backend configuration: {backend.properties}")
    print(f" -- Backend job limit: {backend.job_limit}")

    transpiled_qc = transpile(qc, backend, optimization_level=3)
    job = backend.run(transpiled_qc, shots=1)
    job_monitor(job, interval=2)

    results = job.result()
    print(f"Results: {results}")
    answer = results.get_counts(qc)
    print(f"Answer: {answer}")

    plot_histogram(answer)
    plt.show()


if __name__ == "__main__":
    main()
