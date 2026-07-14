#finding eigenstates and eigenvalues of sigmax
import numpy as np
sigmax = np.array([[0,1],[1,0]])
eigenvalues, eigenvectors = np.linalg.eig(sigmax)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)