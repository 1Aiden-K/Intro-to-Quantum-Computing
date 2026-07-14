import numpy as np
from sklearn.preprocessing import normalize

v1 = np.array([[2],[1+1j]])
print(v1)

v2 = v1/np.linalg.norm(v1)
print(v2)