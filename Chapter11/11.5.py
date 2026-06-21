#checking <h1|h2> = ∑∑<f|e><g|k>
import numpy as np
f = np.array([[1],[1]])
e = np.array([[0],[1]])
g = np.array([[1j],[1j]])
k = np.array([[1j],[1]])

h1 = np.kron(f, e)
h2 = np.kron(g,k)

inner_product_h1_h2 = np.vdot(h1,h2)
inner_product_term2 = np.vdot(f ,e) + np.vdot(g,k)
print(inner_product_term2 == inner_product_h1_h2)
print(inner_product_h1_h2)
print(inner_product_term2)