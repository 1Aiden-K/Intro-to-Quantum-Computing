#entanglement swapping protocol
from quantum_utils import create_bell_pair, bell_measurement, pauli_correction
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import circuit_drawer
from matplotlib import pyplot as plt
from qiskit.circuit import Qubit, Clbit

#demo version
def entanglement_swap_demo(qc: QuantumCircuit,
    alice: Qubit, ancillary: Qubit, bob: Qubit,
    c0: Clbit, c1: Clbit):
    """
    Swaps entanglement from Carlos and Alice to Carlos and Bob.
    Assumes:
        Carlos and Alice are entangled,
        Bob and ancillary are entangled,
    """
    bell_measurement(qc, alice, ancillary, c0, c1)
    qc.barrier()
    pauli_correction(qc, bob, c0, c1)

#demo
if __name__ == "__main__": 
    #qubit labels
    alice = QuantumRegister(1, name='alice')
    ancillary = QuantumRegister(1, name='ancillary')
    bob = QuantumRegister(1, name='bob')
    carlos = QuantumRegister(1, name='carlos')
    #for storing collapsed states of individual qubits, initializes to 0000
    cr = ClassicalRegister(4, "c")


    qc = QuantumCircuit(bob, ancillary, alice, carlos,
                        cr)

    #demo entanglements
    create_bell_pair(qc, carlos, alice)
    qc.barrier()
    create_bell_pair(qc, ancillary, bob)
    qc.barrier()

    entanglement_swap_demo(qc, alice, ancillary, bob, cr[1], cr[2])
    qc.barrier()

    qc.measure(bob, cr[0])
    qc.measure(carlos, cr[3])

    #draw the circuit
    circuit_drawer(qc, output="mpl", style={"backgroundcolor": "#EEEEEE"}, plot_barriers=True)
    plt.show()