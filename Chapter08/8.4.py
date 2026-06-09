#projectors finding probability of eigenstates of sigmax in |0>/|1> basis
import numpy as np
sigmax = np.array([[0,1],[1,0]])
eigenvalues, eigenvectors = np.linalg.eig(sigmax)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

projector_plus = np.outer(np.array([[1],[0]]), np.array([[1],[0]]).T.conjugate())
projector_minus = np.outer(np.array([[0],[1]]), np.array([[0],[1]]).T.conjugate())

a_minus_squared = eigenvectors[:, 0].T.conjugate() @ projector_minus @ eigenvectors[:, 0]
print(f"Probability of measuring |->: {abs(a_minus_squared)}")
a_plus_squared = eigenvectors[:, 1].T.conjugate() @ projector_plus @ eigenvectors[:, 1]
print(f"Probability of measuring |+>: {abs(a_plus_squared)}")