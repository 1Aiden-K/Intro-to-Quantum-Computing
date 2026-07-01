#Creating 2 qubit circuit where a NOT gate is applied to MSB then a CNOT is applied to the two with the MSB being the control qubit
from qiskit import QuantumCircuit

#initiate a 2-qubit circuit
qc = QuantumCircuit(2)

#X gate to the qubit 1 (MSB)
qc.x(1)

#CNOT gate
qc.cx(1,0)

#draw the circuit
print(qc.draw())