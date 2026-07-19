#find grovers algoritm matrices with n=2 and a=3 
import numpy as np

n=2
a=3

H = (1/np.sqrt(2)) * np.array([[1,1],[1, -1]])

H_N = H

for _ in range(n-1):
    H_N = np.kron(H_N, H)

target = np.zeros(2**n)
target[a] = 1

initVector = np.zeros(2**n)
initVector[0] = 1

phi = H_N @ initVector

a_orth = np.zeros(2**n)
for i in range(2**n):
    a_orth[i] = 1
a_orth[a] = 0

a_orth = (1/np.sqrt(2**n-1)) * a_orth