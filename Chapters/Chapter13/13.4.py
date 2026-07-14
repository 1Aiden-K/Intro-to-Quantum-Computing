#inner product between basis states of two electron spins
import numpy as np

one = np.array([[1],[0]])
plus = (1/np.sqrt(2))*np.array([[1],[1]])

print(np.vdot(one, plus))

#if this is between two different electrons, then they belong to different Hilbert spaces, and the inner product should be undefined, but often just shorthanded to 1 apparently.