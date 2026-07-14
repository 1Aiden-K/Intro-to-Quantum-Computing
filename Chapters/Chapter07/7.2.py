#x pauli matrix
import numpy as np

sigmax = np.array([[0,1],[1,0]])

i = np.matmul(sigmax, sigmax)
print(i)