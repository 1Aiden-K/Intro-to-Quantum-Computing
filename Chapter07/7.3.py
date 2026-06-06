#prive sigmay is hermitian
import numpy as np

sigmay = np.array([[0,-1j],[1j,0]])

sigmay_dag = np.conjugate(sigmay).T
print(sigmay, sigmay_dag)
print(np.array_equal(sigmay, sigmay_dag))