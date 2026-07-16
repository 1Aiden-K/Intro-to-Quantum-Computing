#entanglement swapping protocol
from quantum_utils import measure_x
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import circuit_drawer
from matplotlib import pyplot as plt
from qiskit.circuit import Qubit, Clbit, Gate

uf = Gate(name="uf", num_qubits=2, params=[], label="Uf")

def deutsch_algorithm_demo(qc: QuantumCircuit,
    q0: Qubit, q1: Qubit,
    c0: Clbit):
    """
    Creates Deutsch algorithm Ciruit. 
    Assumes q0 and q1 are initialized to 0
    """
    qc.x(q0)
    qc.h(q0)
    qc.h(q1)   
    qc.barrier()

    #this would be some quantum oracle
    qc.append(uf, [q0, q1])
    qc.barrier()

    measure_x(qc, q1, c0)


#demo
if __name__ == "__main__": 
    #qubit
    qr = QuantumRegister(2, "q")
    #for storing collapsed states of individual qubits, initializes to 0000
    cr = ClassicalRegister(2, "c")


    qc = QuantumCircuit(qr,
                        cr)

    deutsch_algorithm_demo(qc, qr[0], qr[1], cr[1])


    #draw the circuit
    circuit_drawer(qc, output="mpl", style={"backgroundcolor": "#EEEEEE"}, plot_barriers=True)
    plt.show()