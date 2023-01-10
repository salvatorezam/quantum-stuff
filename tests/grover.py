from qiskit import QuantumCircuit, Aer
import matplotlib.pyplot as plt


def display_unitary(qc):
    """Simulates a simple circuit and display its matrix representation.
    Args:
        qc (QuantumCircuit): The circuit to compile to a unitary matrix
        prefix (str): Optional LaTeX to be displayed before the matrix
    Returns:
        None (displays matrix as side effect)
    """
    sim = Aer.get_backend("aer_simulator")
    # Next, we'll create a copy of the circuit and work on
    # that so we don't change anything as a side effect
    qc = qc.copy()
    # Tell the simulator to save the unitary matrix of this circuit
    qc.save_unitary()
    unitary = sim.run(qc).result().get_unitary()
    print(unitary)


#
# -------------- oracle ----------------------------
#

oracle = QuantumCircuit(2)
# oracle.cz(0, 1)  # invert phase of |11>
oracle.ccx(0, 1, 2)
oracle.draw(output="mpl")
plt.show()

display_unitary(oracle)


#
# -------------- diffuser --------------------------
#

diffuser = QuantumCircuit(2)
diffuser.h([0, 1])
diffuser.x([0, 1])
diffuser.cz(0, 1)
diffuser.x([0, 1])
diffuser.h([0, 1])
diffuser.draw(output="mpl")
plt.show()


#
# -------------- grover ----------------------------
#

grover = QuantumCircuit(2)
grover.h([0, 1])  # initialise |s>
grover = grover.compose(oracle)
grover = grover.compose(diffuser)
grover.measure_all()
grover.draw(output="mpl")
plt.show()


#
# -------------- running the simulation ------------
#

sim = Aer.get_backend("aer_simulator")
results = sim.run(grover).result().get_counts()
print("Results: ", results)
