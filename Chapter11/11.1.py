#computing tensor product
import numpy as np
f = np.array([[0],[1]])
g = (1/np.sqrt(2))*np.array([[1],[1]])
print(np.kron(f,g))
print(np.kron(g,f))