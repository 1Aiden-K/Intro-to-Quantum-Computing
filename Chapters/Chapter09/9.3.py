import numpy as np

sigmax = np.array([[0,1],[1,0]])
sigmay = np.array([[0,-1j],[1j,0]])
sigmaz = np.array([[1,0],[0,1]])

print(np.linalg.det(sigmax))
print(np.linalg.det(sigmay))
print(np.linalg.det(sigmaz))