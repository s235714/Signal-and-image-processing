print('Hello world!')

# 0, 4pi, 8 kwantow
# https://gist.github.com/xehivs/05c971695846057c76cfab8dbdbdbdd2

import numpy as np
import matplotlib.pyplot as plt

resolution = 4
depth = 4

ls0 = np.linspace(start=0, stop=8 * np.pi, num=resolution)
ls1 = np.linspace(start=0, stop=8 * np.pi, num=resolution*2)
ls2 = np.linspace(start=0, stop=8 * np.pi, num=resolution*4)
ls3 = np.linspace(start=0, stop=8 * np.pi, num=resolution*8)
ls4 = np.linspace(start=0, stop=8 * np.pi, num=resolution*16)
print(ls2)

size = 16, 16
mat = np.zeros(size)
mat[3:5, 2:4] = 1
#print(mat)

fig, ax = plt.subplots(5, 5, figsize=(15, 10))
#ax[0][1].plot(ls2, c='red', ls=':', label='CZERWONA LINIA')
#ax[0][1].legend()


#ax[1][0].imshow(mat, cmap='binary')

sinus0 = np.sin(ls0)
#ax[0][0].grid(ls0 = ':') #siatka
ax[0][0].plot(sinus0)
ax[0][0].spines['right'].set_visible(False) #brak linii po prawej
ax[0][0].spines['top'].set_visible(False) #brak linii na gorze

sinus1 = np.sin(ls1)
ax[1][0].plot(sinus1)
ax[1][0].spines['right'].set_visible(False)
ax[1][0].spines['top'].set_visible(False)

sinus2 = np.sin(ls2)
ax[2][0].plot(sinus2)
ax[2][0].spines['right'].set_visible(False)
ax[2][0].spines['top'].set_visible(False)

sinus3 = np.sin(ls3)
ax[3][0].plot(sinus3)
ax[3][0].spines['right'].set_visible(False)
ax[3][0].spines['top'].set_visible(False)

sinus4 = np.sin(ls4)
ax[4][0].plot(sinus4)
ax[4][0].spines['right'].set_visible(False)
ax[4][0].spines['top'].set_visible(False)

hm0 = sinus0[:,np.newaxis] * sinus0[np.newaxis:]
hm0 = (hm0 + 1)/2
hm0 -= np.min(hm0)
hm0 /= np.max(hm0)
ax[0][1].imshow(hm0, cmap='binary', vmin=0, vmax=1)

hm1 = sinus1[:,np.newaxis] * sinus0[np.newaxis:]
hm1 = (hm1 + 1)
hm1 -= np.min(hm1)
hm1 /= np.max(hm1)
ax[1][1].imshow(hm1, cmap='binary', vmin=0, vmax=1)

hm2 = sinus2[:,np.newaxis] * sinus2[np.newaxis:]
hm2 = (hm2 + 1)/2
hm2 -= np.min(hm2)
hm2 /= np.max(hm2)
ax[2][1].imshow(hm2, cmap='binary', vmin=0, vmax=1)

hm3 = sinus3[:,np.newaxis] * sinus3[np.newaxis:]
hm3 = (hm3 + 1)/2
hm3 -= np.min(hm3)
hm3 /= np.max(hm3)
ax[3][1].imshow(hm3, cmap='binary', vmin=0, vmax=1)

hm4 = sinus4[:,np.newaxis] * sinus4[np.newaxis:]
hm4 = (hm4 + 1)/2
hm4 -= np.min(hm4)
hm4 /= np.max(hm4)
ax[4][1].imshow(hm4, cmap='binary', vmin=0, vmax=1)

nrange = (-2, 2)
norm_image = (hm0 - nrange[0]) / (nrange[1] - nrange[0])
norm_image = np.clip(hm0, 0, 1)
ax[0][2].imshow(norm_image, cmap='binary', vmin=0, vmax=1)

#ax[0][2].plot(ls2, sinus2)
#ax[0][2].set_xlabel('X')
#ax[0][2].set_ylabel('Y')



nrange = (-2, 2)
norm_image = (hm2 - nrange[0]) / (nrange[1] - nrange[0])
norm_image = np.clip(hm2, 0, 1)
ax[1][3].imshow(norm_image, cmap='binary', vmin=0, vmax=1)

dmin, dmax = (0, np.power(2, depth) - 1)
digital_image = np.rint(norm_image * dmax)
ax[1][4].imshow(digital_image, cmap='binary')


plt.tight_layout()
plt.savefig('foo2.png')
