from qiskit import QuantumCircuit, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

backend = Aer.get_backend("aer_simulator")

#
# -------------- Charlie's circuit ------------
#

qc_charlie = QuantumCircuit(2, 2)
qc_charlie.ry(1.911, 1)
qc_charlie.cx(1, 0)
qc_charlie.ry(0.785, 0)
qc_charlie.cx(1, 0)
qc_charlie.ry(2.356, 0)

qc_charlie.draw(output="mpl")
plt.show()


#
# -------------- Alice and Bob's z measurement ------------
#

meas_zz = QuantumCircuit(2, 2)
meas_zz.measure([0, 1], [0, 1])

meas_zz.draw(output="mpl")
plt.show()

# Results for z measurements:
#
# this shows that the qubits never both output 0 for z measurements
#
counts = backend.run(qc_charlie.compose(meas_zz)).result().get_counts()
plot_histogram(counts)
plt.show()


#
# -------------- Alice z measurement and Bob's x measurement ------------
#

meas_zx = QuantumCircuit(2, 2)
meas_zx.h(0)
meas_zx.measure([0, 1], [0, 1])
meas_zx.h(0)

meas_zx.draw(output="mpl")
plt.show()

# Results for a z (Alice) and an x (Bob) measurement:
#
# in this case the qubits never both output 1
#
counts = backend.run(qc_charlie.compose(meas_zx)).result().get_counts()
plot_histogram(counts)
plt.show()


#
# -------------- Alice x measurement and Bob's z measurement ------------
#

meas_xz = QuantumCircuit(2, 2)
meas_xz.h(0)
meas_xz.measure([0, 1], [0, 1])
meas_xz.h(0)

meas_xz.draw(output="mpl")
plt.show()

# Results for a z (Bob) and an x (Alice) measurement:
#
counts = backend.run(qc_charlie.compose(meas_xz)).result().get_counts()
plot_histogram(counts)
plt.show()

# The following informations have been acquired:
# 1. If z measurements are made on both qubits, they never both output 0;
# 2. If an x measurement of one qubit outputs 1, a z measurement of the other will output 0 (because the 11 result never occurs in these cases).


#
# -------------- Alice x measurement and Bob's z measurement ------------
#

meas_xx = QuantumCircuit(2, 2)
meas_xx.h([0, 1])
meas_xx.measure([0, 1], [0, 1])
meas_xx.h(0)

meas_xz.draw(output="mpl")
plt.show()

# Results for x measurements:
#
counts = backend.run(qc_charlie.compose(meas_xx)).result().get_counts()
plot_histogram(counts)
plt.show()
