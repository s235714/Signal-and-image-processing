import numpy as np
import matplotlib.pyplot as plt

resolution = 256
size = 32
depth = 2
drange = (-1, 1)
n_iter =  256
N = np.power(2, depth) - 1
prober = np.linspace(start=0, stop=8*np.pi, num=resolution)
sinus = np.sin(prober)
perfect_image = sinus[:, np.newaxis] * sinus[np.newaxis:]
n_matrix = np.zeros(perfect_image.shape)
o_matrix = np.zeros(perfect_image.shape)

fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(12, 8))

for i in range (n_iter):
    noise = np.random.normal(0,1,size=(resolution,resolution))
    n_image = np.add(perfect_image, noise)
    o_image = perfect_image
    n_dimg = (n_image - drange[0]) / (drange[1] - drange[0])
    o_dimg = (o_image - drange[0]) / (drange[1] - drange[0])
    n_dimg = np.clip(n_dimg, 0, 1)
    o_dimg = np.clip(o_dimg, 0, 1)

    n_dimg = np.rint(n_dimg * N)
    o_dimg = np.rint(o_dimg * N)

    n_matrix = n_matrix + n_dimg
    o_matrix = o_matrix + o_dimg

    axs[0][0].imshow(perfect_image, cmap='binary')
    axs[0][1].imshow(noise, cmap='binary')

    axs[1][0].imshow(o_dimg, cmap='binary')
    axs[1][1].imshow(n_dimg, cmap='binary')

    axs[2][0].imshow(o_matrix, cmap='binary')
    axs[2][1].imshow(n_matrix, cmap='binary')

plt.tight_layout()
plt.savefig('obraz.png')
