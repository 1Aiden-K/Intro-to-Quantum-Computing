# (HH)(IX)|0>|0>
import numpy as np

H = (1/np.sqrt(2)) * np.array([[1,1],[1, -1]])
I = np.array([[1,0],[0,1]])
X = np.array([[0,1],[1,0]])
ZERO = np.array([1,0])

operator = (np.kron(H,H)) @ (np.kron(I, X))

matrix = operator @ np.kron(ZERO, ZERO)