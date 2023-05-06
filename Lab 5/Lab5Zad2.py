import numpy as np
import matplotlib.pyplot as plt
import skimage

image = skimage.data.chelsea()
image = np.mean(image, axis=1).astype(np.uint8)
skip = 10
image = image[::skip, ::skip]

source_values = image.reshape(-1)
height, width = image.shape
aspect = height/width

x_source_space = np.linspace(0, 1, height)
y_source_space = np.linspace(0, aspect, width)

A = np.ones(np.meshgrid(x_source_space,y_source_space))
T = np.array([
                [np.cos(np.pi/4), -np.sin(np.pi/4),0],
                [np.sin(np.pi/4),  np.cos(np.pi/4),0],
                [0         ,0           ,1]
            ]),

plt.imshow(image)
plt.savefig('Obraz_chelsea.png')
