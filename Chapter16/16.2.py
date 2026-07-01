#show that controlled z gate converts |-> to |+>
import numpy as np

#get phase shift matrix in c4
def controlledPSGate(iota):
    return np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,np.exp(1j*iota)]])

controlledZGate = controlledPSGate(np.pi)

minus = (1/np.sqrt(2))*np.array([[1],[-1]])
plus = (1/np.sqrt(2))*np.array([[1],[1]])

one = np.array([[0],[1]])

print (np.allclose(controlledZGate @ np.kron(one, minus), np.kron(one, plus)))