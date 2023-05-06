print('Hello world!')

# 0, 4pi, 8 kwantow

import numpy as np
import matplotlib.pyplot as plt

resolution = 32
depth = 4

ls = np.linspace(start=0, stop=4 * np.pi, num=resolution)
print(ls)

size = 16, 16
mat = np.zeros(size)
mat[3:6, 2:9] = 1

# print(mat)

fig, ax = plt.subplots(2, 3, figsize=(10, 5))
ax[0][0].plot(ls, c='red', ls=':', label='CZERWONA LINIA')
ax[0][0].legend()


ax[1][0].imshow(mat, cmap='binary')

sinus = np.sin(ls)
ax[0][1].plot(sinus)
ax[0][1].spines['right'].set_visible(False)
ax[0][1].spines['top'].set_visible(False)
ax[0][1].set_xlabel('X')
ax[0][1].set_ylabel('Y')

ax[0][2].plot(ls, sinus)

hm = sinus[:,np.newaxis] * sinus[np.newaxis:]
ax[1][0].imshow(hm, cmap='binary', vmin=0, vmax=1)

nrange = (-2, 2)
norm_image = (hm - nrange[0]) / (nrange[1] - nrange[0])
norm_image = np.clip(norm_image, 0, 1)
ax[1][1].imshow(norm_image, cmap='binary', vmin=0, vmax=1)

dmin, dmax = (0, np.power(2, depth) - 1)
digital_image = np.rint(norm_image * dmax)
ax[1][2].imshow(digital_image, cmap='binary')


plt.tight_layout()
plt.savefig('foo.png')
