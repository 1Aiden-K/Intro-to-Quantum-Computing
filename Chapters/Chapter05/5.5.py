import numpy as np

v1_pm = np.array([[1],[2]]) #in |+>/|-> basis
v1_pm = v1_pm / np.linalg.norm(v1_pm) #normalize

H = np.array([[1,  1], #hadamard matrix
              [1, -1]]) / np.sqrt(2) #changes basis from |+>/|-> to |0>/|1>


v1_10 = H @ v1_pm #change basis to |0>/|1>

print(f"{v1_10} |0>/|1> basis")

print(f"{v1_pm} |+>/|-> basis")

v1_10 = np.array([[0],[1]]) #collapsed to |1>

v1_pm = H @ v1_10 #change basis back to |+>/|->

print(f"{v1_pm} |+>/|-> basis")

print(f"Odds of getting |+>: {abs(v1_pm[0][0]**2)}") #probability = a^2