# initialization
import matplotlib.pyplot as plt
import numpy as np

# importing Qiskit
from qiskit import IBMQ, Aer, assemble, transpile
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.ibmq import least_busy

# import basic plot tools
from qiskit.visualization import plot_histogram


# --------------------- Building the circuit with 2 qubits ---------------------------------

n = 2
grover_circuit = QuantumCircuit(n)


def initialize_s(qc, qubits):
    """Apply a H-gate to 'qubits' in qc"""
    for q in qubits:
        qc.h(q)
    return qc


grover_circuit = initialize_s(grover_circuit, [0, 1])
grover_circuit.cz(0, 1)  # Oracle


# Diffusion operator (U_s)
grover_circuit.h([0, 1])
grover_circuit.z([0, 1])
grover_circuit.cz(0, 1)
grover_circuit.h([0, 1])
grover_circuit.draw(output="mpl")
# plt.show()


# --------------------------------------- Simulation ---------------------------------------

sim = Aer.get_backend("aer_simulator")
# we need to make a copy of the circuit with the 'save_statevector'
# instruction to run on the Aer simulator
grover_circuit_sim = grover_circuit.copy()
grover_circuit_sim.save_statevector()
qobj = assemble(grover_circuit_sim)
result = sim.run(qobj).result()
statevec = result.get_statevector()

# from qiskit_textbook.tools import vector2latex
# vector2latex(statevec, pretext="|\\psi\\rangle =")


grover_circuit.measure_all()

aer_sim = Aer.get_backend("aer_simulator")
# qobj = assemble(grover_circuit) # deprecated run(qobj)
result = aer_sim.run(grover_circuit).result()
counts = result.get_counts()
plot_histogram(counts)
plt.show()


# --------------------------------------- Computation on quantum hardware ------------------

IBMQ.enable_account(
    "61f771f68198fd1471e5e762201b8e61c6d051e81e01980f8bc16f748fe36ddac9d385ccd000c3e87312aff0decf10c7681a8b80b25379d6590fda1af07a6871"
)
IBMQ.save_account(
    "61f771f68198fd1471e5e762201b8e61c6d051e81e01980f8bc16f748fe36ddac9d385ccd000c3e87312aff0decf10c7681a8b80b25379d6590fda1af07a6871"
)

# Load IBM Q account and get the least busy backend device
provider = IBMQ.load_account()
provider = IBMQ.get_provider("ibm-q")
device = least_busy(
    provider.backends(
        filters=lambda x: x.configuration().n_qubits >= 3
        and not x.configuration().simulator
        and x.status().operational == True
    )
)
print("Running on current least busy device: ", device)

# Run our circuit on the least busy backend. Monitor the execution of the job in the queue
from qiskit.tools.monitor import job_monitor

transpiled_grover_circuit = transpile(grover_circuit, device, optimization_level=3)
job = device.run(transpiled_grover_circuit)
job_monitor(job, interval=2)

# Get the results from the computation
results = job.result()
answer = results.get_counts(grover_circuit)
plot_histogram(answer)
plt.show()
