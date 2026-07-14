#swap gate implementation 2 ways
import numpy as np

cnotMSB = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
cnotLSB = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])

print (cnotMSB @ cnotLSB @ cnotMSB == cnotLSB @ cnotMSB @ cnotLSB)