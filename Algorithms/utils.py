from qiskit import QuantumCircuit
from qiskit.circuit import Qubit, Clbit

def create_bell_pair(qc: QuantumCircuit, 
                     q0: Qubit, q1: Qubit):
    """
    Creates bell pair between two qubits with q0 as control and q1 as target.
    """
    qc.h(q0)
    qc.cx(q0, q1)
    qc.barrier()

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
    qc.barrier()

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
    qc.barrier()

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