from qiskit import QuantumCircuit, Aer
import matplotlib.pyplot as plt

#
# -------------- third party -----------------------
#

qc_charlie = QuantumCircuit(2, 2)

qc_charlie.h(1)
qc_charlie.cx(1, 0)

qc_charlie.draw(output="mpl")
plt.show()

#
# -------------- alice -----------------------------
#

MESSAGE = "01"

qc_alice = QuantumCircuit(2, 2)

if MESSAGE[-2] == "1":
    qc_alice.x(1)
if MESSAGE[-1] == "1":
    qc_alice.z(1)

qc_alice.draw(output="mpl")
plt.show()


#
# -------------- bob -------------------------------
#

qc_bob = QuantumCircuit(2, 2)

qc_bob.cx(0, 1)
qc_bob.h(0)

qc_bob.measure([0, 1], [0, 1])

qc_bob.draw(output="mpl")
plt.show()


#
# -------------- channel ---------------------------
#

backend = Aer.get_backend("aer_simulator")

complete_qc = qc_charlie.compose(qc_alice.compose(qc_bob))
result = backend.run(complete_qc).result().get_counts()

print(result)
