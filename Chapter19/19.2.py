import numpy as np

hadamard = np.array([[1,1],[1, -1]])
identity = np.array([[1,0],[0,1]])
cnot = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])

matrix = np.kron(hadamard, identity) @ cnot @ np.kron(identity, hadamard)

print(matrix)