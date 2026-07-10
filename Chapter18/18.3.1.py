#implement IxX with qiskit
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import circuit_drawer, plot_histogram
from matplotlib import pyplot as plt
from qiskit_aer import AerSimulator


qc = QuantumCircuit(2)

qc.x(0) # setting the start to |01> state
qc.id(1) #identity

#SWAP circuit
qc.cx(1,0)
qc.cx(0,1)
qc.cx(1,0)

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