#implement SWAP gate using 3 CNOT gates
import numpy as np

cnotMSB = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
cnotLSB = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
swapGate = cnotMSB @ cnotLSB @ cnotMSB

print(swapGate)