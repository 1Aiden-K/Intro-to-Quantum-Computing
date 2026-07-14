#checking tensor product distribution rule
import numpy as np
f = np.array([[0],[1]])
g = (1/np.sqrt(2))*np.array([[1],[1]])
e = np.array([[1],[0]])

print(np.kron(f + e,g) == np.kron(f,g) + np.kron(e, g))