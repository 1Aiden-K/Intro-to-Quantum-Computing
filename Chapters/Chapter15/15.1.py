#show that UNOT is unitary
import numpy as np

UNOT = np.array([[0,1],[1,0]])
UNOT_dagger = np.conjugate(np.transpose(UNOT))

print(UNOT_dagger == UNOT)