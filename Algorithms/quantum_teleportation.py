#quantum teleportation protocol
from Algorithms.utils import create_bell_pair, bell_measurement, pauli_correction
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import circuit_drawer
from matplotlib import pyplot as plt
from qiskit.circuit import Qubit, Clbit

def teleport(qc: QuantumCircuit,
            alice: Qubit, ancillary: Qubit, bob: Qubit, 
            c0: Clbit, c1: Clbit):
    """
    Teleports Alice's state to Bob, collapsing Alice in the process.
    Assumes:
        Bob and ancillary are entangled
    """
    bell_measurement(qc, alice, ancillary, c0, c1)
    pauli_correction(qc, bob, c0, c1)

    
#demo
if __name__ == "__main__":
    #qubit labels
    alice = QuantumRegister(1, name='alice')
    ancillary = QuantumRegister(1, name='ancillary')
    bob = QuantumRegister(1, name='bob')
    #for storing collapsed states of individual qubits, initializes to 0000
    cr = ClassicalRegister(3, "c")

    qc = QuantumCircuit(bob, ancillary, alice, cr)

    #demo entanglement
    create_bell_pair(qc, ancillary, bob)

    teleport(qc, alice, ancillary, bob, cr[1], cr[2])

    qc.measure(bob, cr[0])
    
    #draw the circuit
    circuit_drawer(qc, output="mpl", style={"backgroundcolor": "#EEEEEE"}, plot_barriers=True)
    plt.show()