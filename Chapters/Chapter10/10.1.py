#find unitary matrix of sigmax to sigmay
import numpy as np
sigmax = np.array([[0,1],[1,0]])

plus_x = (1/np.sqrt(2))*np.array([[1],[1]])
minus_x = (1/np.sqrt(2))*np.array([[1],[-1]])

plus_y = (1/np.sqrt(2))*np.array([[1],[1j]])
minus_y = (1/np.sqrt(2))*np.array([[1],[-1j]])

U_yTox = np.array([
    [np.vdot(plus_x, plus_y), np.vdot(plus_x, minus_y)], 
    [np.vdot(minus_x, plus_y), np.vdot(minus_x, minus_y)]])
print(U_yTox)