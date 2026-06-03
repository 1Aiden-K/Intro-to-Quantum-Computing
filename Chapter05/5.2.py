import numpy as np

v1 = np.array([[1],[2]])

v1norm = v1 / np.linalg.norm(v1)
print(v1norm)