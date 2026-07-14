#construct sigmax from eigenvectors and eigenvalues
import numpy as np
#yes, this defeats the purpose of the exercise, but its a quick way to get the eigenvectors and eigenvalues without having to type them out
eigenvalues, eigenvectors = np.linalg.eig(np.array([[0,1],[1,0]]))

sigmax_reconstructed = np.zeros((2,2), dtype=complex)

for i in range(len(eigenvalues)):
    sigmax_reconstructed += eigenvalues[i] * np.outer(eigenvectors[:,i], eigenvectors[:,i].T.conjugate())

print("Reconstructed sigmax:\n", sigmax_reconstructed)