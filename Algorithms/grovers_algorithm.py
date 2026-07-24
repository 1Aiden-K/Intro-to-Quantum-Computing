from quantum_utils import h_all, grover_mixer
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import circuit_drawer
from matplotlib import pyplot as plt
from qiskit.circuit import Qubit, Clbit, Gate

def grovers_algorithm_demo(qc: QuantumCircuit,
    q0: Qubit, q1: Qubit,
    oracle: Gate,
    c0: Clbit, c1: Clbit):
    """
    Creates Grover's algorithm Ciruit on two qubits. 
    Assumes: 
    q0 and q1 are initialized to 0, 
    oracle is a 2 qubit gate
    """

    h_all(qc, [q0, q1])
    qc.barrier()

     #this would be some quantum oracle
    qc.append(oracle, [q0, q1])
    qc.barrier()

    grover_mixer(qc, q0, q1)
    qc.barrier()

    qc.measure(q0, c0)
    qc.measure(q1, c1)


#demo
if __name__ == "__main__": 
    oracle = Gate(name="oracle", num_qubits=2, params=[], label="Uf")
    #qubit
    qr = QuantumRegister(2, "q")
    #for storing collapsed states of individual qubits, initializes to 0000
    cr = ClassicalRegister(2, "c")


    qc = QuantumCircuit(qr,
                        cr)

    grovers_algorithm_demo(qc, qr[0], qr[1], oracle, cr[0], cr[1])


    #draw the circuit
    circuit_drawer(qc, output="mpl", style={"backgroundcolor": "#EEEEEE"}, plot_barriers=True)
    plt.show()