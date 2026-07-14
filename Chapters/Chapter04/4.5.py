import matplotlib.pyplot as plt
import numpy as np

v1 = np.array([1/np.sqrt(2), 1/np.sqrt(2)])  # real vector
v2 = np.array([1/np.sqrt(2), -1/np.sqrt(2)])  # real vector

fig, ax = plt.subplots(figsize=(6, 6))  # fixed 6x6 inches
ax.set_aspect('equal')
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='blue')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()