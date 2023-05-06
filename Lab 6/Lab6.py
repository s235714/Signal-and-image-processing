import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import disk, erosion, dilation, opening, closing

image = np.zeros(shape = (32,64))

x = np.random.randint(0,31,256)
y = np.random.randint(0,63,256)
image[x,y] = 1
image[x-1,y] = 1
image[x,y + 1] = 1

image = dilation(image, np.array([[1,0],[1,1]]))

fig, axs = plt.subplots(nrows=4, ncols=3)
axs[0][0].imshow(image)

selen = disk(1)
axs[0][1].imshow(selen)

erode = erosion(image, selen)
axs[1][0].imshow(erode)

dilate = dilation(image, selen)
axs[1][1].imshow(dilate)

op = opening(image, selen)
axs[2][0].imshow(op)

cl = closing(image, selen)
axs[2][1].imshow(cl)

cube = np.zeros(shape = (32,64,3))
cube[:, :, 0] = image
cube[:, :, 1] = op
cube[:, :, 2] = cl
axs[3][0].imshow(cube)


plt.tight_layout()
plt.savefig('obraz.png')
