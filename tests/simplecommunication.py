from qiskit import QuantumCircuit, Aer
import matplotlib.pyplot as plt

#
# -------------- sender -----------------------
#

# the message to be sent
MESSAGE = "00"

# Alice encodes the message
qc_alice = QuantumCircuit(2, 2)
if MESSAGE[-1] == "1":
    qc_alice.x(0)
if MESSAGE[-2] == "1":
    qc_alice.x(1)

qc_alice.draw(output="mpl")
plt.show()


#
# -------------- receiver -----------------------
#

# Bob measures
qc_bob = QuantumCircuit(2, 2)
qc_bob.measure([0, 1], [0, 1])

qc_bob.draw(output="mpl")
plt.show()

#
# -------------- channel -----------------------
#

backend = Aer.get_backend("aer_simulator")
received_message = backend.run(qc_alice.compose(qc_bob)).result().get_counts()

print("Bob received: ", received_message)
