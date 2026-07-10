#implement Uxor(H x I) with qiskit
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import circuit_drawer, plot_histogram
from matplotlib import pyplot as plt
from qiskit_aer import AerSimulator


qc = QuantumCircuit(2)

#little endian, putting identity on the lsb
qc.id(0) #identity
qc.h(1) #hadamard
qc.cx(1, 0) # cnot

qc.measure_all()

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