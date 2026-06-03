import numpy as np

v1_pm = np.array([[1],[2]]) #in |+>/|-> basis
v1_pm = v1_pm / np.linalg.norm(v1_pm) #normalize

H = np.array([[1,  1], #hadamard matrix
              [1, -1]]) / np.sqrt(2) #changes basis from |+>/|-> to |0>/|1>


v1_10 = H @ v1_pm #change basis to |0>/|1>

print(v1_10)
print(v1_10.shape)
print(np.linalg.norm(v1_10)) #gets magnitude of vector, should be 1 since we normalized it before