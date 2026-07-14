import numpy as np

v1 = np.array([[1j],[2]])
print(v1)
print(v1.shape)

v2 = v1/np.linalg.norm(v1)
print(v2)

print(np.vdot(v2, v2))
v2_t = np.conjugate(v2).T
print(v2_t)
print(v2_t.shape)
print(np.dot(v2_t, v2))