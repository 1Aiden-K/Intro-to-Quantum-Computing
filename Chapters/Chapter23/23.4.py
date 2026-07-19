#continue with 23.3
import numpy as np

N=2
A=3

H = (1/np.sqrt(2)) * np.array([[1,1],[1, -1]])

H_N = H
for _ in range(N-1):
    H_N = np.kron(H_N, H)

I = np.eye(N)

TARGET = np.zeros(2**N)
TARGET[A] = 1

initVector = np.zeros(2**N)
initVector[0] = 1

phi = H_N @ initVector

a_orth = np.zeros(2**N)
for i in range(2**N):
    a_orth[i] = 1
a_orth[A] = 0

a_orth = (1/np.sqrt(2**N-1)) * a_orth

V = I - 2 * (TARGET @ TARGET.conj().T)
