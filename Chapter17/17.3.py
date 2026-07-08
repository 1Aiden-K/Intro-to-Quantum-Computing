#find H^2 |2> using matrix multiplication
import numpy as np

two = np.array([[0], [0], [1],[0]])

H = 1/(2**(1/2)) * np.array([[1, 1], [1, -1]])

H2 = np.kron(H, H)

final_state = H2 @ two

print(final_state)