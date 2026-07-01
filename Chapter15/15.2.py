#show that UNOT is unitary
import numpy as np

UCNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
UCNOT_dagger = np.conjugate(np.transpose(UCNOT))

print(UCNOT_dagger == UCNOT)