import numpy as np

v1 = np.array([[np.sqrt(3)],[1]])
v2 = np.array([[1],[1]])

inner_product = np.vdot(v1.T, v2)
print(inner_product)