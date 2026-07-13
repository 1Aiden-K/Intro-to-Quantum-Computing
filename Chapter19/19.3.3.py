#simplified quantum teleportation algorithm
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import circuit_drawer, plot_histogram
from matplotlib import pyplot as plt
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2,2)

qc.cx(1,0)
qc.h(1)

qc.measure(1,1)

qc.z(0)
qc.measure(0,0)

#draw the circuit
circuit_drawer(qc, output="mpl", style={"backgroundcolor": "#EEEEEE"})
plt.show()

#simulate
sim = AerSimulator()
compiled = transpile(qc, sim)

result = sim.run(compiled, shots=1024).result()
counts = result.get_counts()

print(counts)
plot_histogram(counts)
plt.show()