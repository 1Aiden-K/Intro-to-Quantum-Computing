#find H^2 |2>
import numpy as np

two = np.array([[0], [0], [1],[0]])
two_msb = 1
two_lsb = 0

final_state = np.zeros((4, 1), dtype=complex)

for i in range(4):
    i_binary = format(i, '02b')
    i_msb = int(i_binary[0])
    i_lsb = int(i_binary[1])

    x = np.zeros((4, 1), dtype=complex)
    x[i, 0] = 1

    xANDy = (two_msb * i_msb) ^ (two_lsb * i_lsb)

    final_state += ((-1) ** int(xANDy)) * x

print(1/(2**1) * final_state)