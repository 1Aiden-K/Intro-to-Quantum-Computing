#show that the eigenvalues of sigmax form a complete basis
import numpy as np
sigmax = np.array([[0,1],[1,0]])
eigenvalues, eigenvectors = np.linalg.eig(sigmax)

sum = np.zeros((2,2), dtype=complex)

for i in eigenvectors:
    sum += np.outer(i, i.T.conjugate())
#should be I
print("Sum of eigenvectors:\n", sum)