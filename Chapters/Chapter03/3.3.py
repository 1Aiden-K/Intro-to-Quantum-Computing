import numpy as np

v1 = np.array([[1j],[1]])
v2 = np.array([[-1j],[1]])

inner_product = np.dot(v1.T, v2)
print(inner_product)