from qiskit import QuantumCircuit
from qiskit.circuit import Qubit, Clbit

def create_bell_pair(qc: QuantumCircuit, 
                     q0: Qubit, q1: Qubit):
    """
    Creates bell pair between two qubits with q0 as control and q1 as target.
    """
    qc.h(q0)
    qc.cx(q0, q1)

def bell_measurement(qc: QuantumCircuit,
                     q0: Qubit, q1: Qubit,
                     c0: Clbit, c1: Clbit):
    """
    Perform a Bell-basis measurement on q0 and q1 with q0 as control and q1 as target.
    Stores the results in c0 and c1 respectively.
    """
    qc.cx(q0, q1)
    qc.measure(q1, c1)
    qc.h(q0)
    qc.measure(q0, c0)

def pauli_correction(qc: QuantumCircuit,
                     target: Qubit,
                     c0: Clbit,c1: Clbit):
    """
    Applies Pauli correction to target qubit.
    """
    with qc.if_test((c1, 1)):
        qc.x(target)
    with qc.if_test((c0, 1)):
        qc.z(target)

def measure_x(qc: QuantumCircuit,
                     q0: Qubit, 
                     c0: Clbit):
    """
    Measures |+>/|-> as |0>/|1> (i.e. sigma_x)
    """
    qc.h(q0)
    qc.measure(q0, c0)

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

def entanglement_swap(qc: QuantumCircuit,
    alice: Qubit, ancillary: Qubit, bob: Qubit,
    c0: Clbit, c1: Clbit):
    """
    Swaps entanglement from Carlos and Alice to Carlos and Bob.
    Assumes:
        Carlos and Alice are entangled,
        Bob and ancillary are entangled,
    """
    bell_measurement(qc, alice, ancillary, c0, c1)
    pauli_correction(qc, bob, c0, c1)