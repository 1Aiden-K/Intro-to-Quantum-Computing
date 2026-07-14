#apply sigmax to |f> tensor |g> in two ways
import numpy as np
f = np.array([[0],[1]])
g = (1/np.sqrt(2))*np.array([[1],[1j]])

sigmax = np.array([[0,1],[1,0]])

product1 = np.kron(sigmax @ f, sigmax @ g)
product2 = np.kron(sigmax, sigmax) @ np.kron(f, g)

print(product1)
print(product2)