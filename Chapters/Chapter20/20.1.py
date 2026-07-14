#calculate |alice> tensor |phi_plus>
import numpy as np

phi_plus = (1/np.sqrt(2)) * np.array([[1, 0, 0, 1]])
alice = np.array([1, 0])#in the form of alpha|0> + beta|1>

print(np.kron(alice, phi_plus))