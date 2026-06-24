#prove that bell states phi_minus, psi_plus, and psi_minus are entangled states
import numpy as np

#for reference
phi_minus = (1/np.sqrt(2))*np.array([[1],[0],[0],[-1]])
psi_plus = (1/np.sqrt(2))*np.array([[0],[1],[1],[0]])
psi_minus = (1/np.sqrt(2))*np.array([[0],[1],[-1],[0]])

phi_minus = (1/np.sqrt(2))*np.array([[1,0],[0,-1]])
psi_plus = (1/np.sqrt(2))*np.array([[0,1],[1,0]])
psi_minus = (1/np.sqrt(2))*np.array([[0,1],[-1,0]])

#if not entangled, then the rank should be 1
print(np.linalg.matrix_rank(phi_minus))
print(np.linalg.matrix_rank(psi_plus))
print(np.linalg.matrix_rank(psi_minus))