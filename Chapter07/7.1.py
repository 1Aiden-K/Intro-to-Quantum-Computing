#y pauli matrix
import numpy as np

sigmay = np.array([[0,-1j],[1j,0]])

i = np.matmul(sigmay, sigmay)
print(i)