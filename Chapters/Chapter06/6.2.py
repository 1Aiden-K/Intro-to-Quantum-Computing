import numpy as np
sigmay = np.array([[0,-1j],[1j,0]])
print(sigmay)
eigvals, eigvecs = np.linalg.eig(sigmay)
print(eigvals)
print(eigvecs)