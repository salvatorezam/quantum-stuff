from qiskit import QuantumCircuit, Aer
import matplotlib.pyplot as plt
from math import pi

backend = Aer.get_backend("aer_simulator")

#
# -------------- x (standard) measurement ------------
#

meas_x = QuantumCircuit(1, 1)
meas_x.h(0)
meas_x.measure(0, 0)

meas_x.draw(output="mpl")
plt.show()


#
# -------------- z measurement -----------------------
#

meas_z = QuantumCircuit(1, 1)
meas_z.measure(0, 0)

meas_z.draw(output="mpl")
plt.show()


#
# -------------- starting state: |0> ----------------------
#

qc = QuantumCircuit(1, 1)

print(
    "Results from z measurement from |0>:",
    backend.run(qc.compose(meas_z)).result().get_counts(),
)

print(
    "Results from x measurement from |0>:",
    backend.run(qc.compose(meas_x)).result().get_counts(),
)


#
# -------------- starting state: |1> ----------------------
#

qc1 = QuantumCircuit(1, 1)
qc1.x(0)

for basis, circ in [("z", meas_z), ("x", meas_x)]:
    print(
        "Results from " + basis + " measurement from |1>:",
        backend.run(qc1.compose(circ)).result().get_counts(),
    )


#
# -------------- starting state: |+> ----------------------
#

qc2 = QuantumCircuit(1, 1)
qc2.h(0)

for basis, circ in [("z", meas_z), ("x", meas_x)]:
    print(
        "Results from " + basis + " measurement from |+>:",
        backend.run(qc2.compose(circ)).result().get_counts(),
    )


#
# -------------- starting state: ry-rotated ----------------------
#

qc3 = QuantumCircuit(1, 1)
qc3.ry(-pi / 4, 0)

for basis, circ in [("z", meas_z), ("x", meas_x)]:
    print(
        "Results from " + basis + " measurement from ry-rot:",
        backend.run(qc3.compose(circ)).result().get_counts(),
    )
