#finding sigmay|0> and <0|sigmay
import numpy as np

#ket
zerospin = np.array([[1],[0]])

sigmay = np.array([[0,-1j],[1j,0]])

#sigmay|0>
print(np.dot(sigmay, zerospin))

zerospin_bra = zerospin.T

#<0|sigmay
print(np.dot(zerospin_bra, sigmay))