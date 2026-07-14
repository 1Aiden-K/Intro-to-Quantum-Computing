#show that z gate converts |-> to |+>
import numpy as np

#get phase shift matrix in c2
def psgate(iota):
    return np.array([[1,0],[0,np.exp(1j*iota)]])

#z gate when iota = pi
zgate = psgate(np.pi)

minus = (1/np.sqrt(2))*np.array([[1],[-1]])
plus = (1/np.sqrt(2))*np.array([[1],[1]])

print (np.allclose(zgate @ minus, plus))