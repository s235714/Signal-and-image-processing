import skimage
import matplotlib.pyplot as plt
import numpy as np

chels = skimage.data.chelsea()[:, :, 0]

# noise = np.random.uniform(
#     low=-512,
#     high=512,
#     size=(*chels.shape, 1000)
# )
#
# noised = noise + chels[:,:,:,np.newaxis]
# denoised = np.mean(noised, axis=3)
# denoised /= np.max(noised)
#
# plt.imshow(denoised)
# plt.savefig('foo.png')


fig, ax = plt.subplots(8, 2, figsize=(20, 20))


translation = np.linspace(0, 255, 256).astype(int)
t_image = translation[chels]
ax[0, 1].imshow(t_image, cmap="Reds_r")

translation = np.linspace(255, 0, 256).astype(int)
t_image = translation[chels]
ax[1, 1].imshow(t_image, cmap="Reds_r")

translation = np.zeros((256,))
translation[100:150] = 1
t_image = translation[chels]
ax[2, 1].imshow(t_image, cmap="Reds_r")

for i in range(3, 6):
    translation = np.sin(np.linspace(0, (i-2)*np.pi, 256))
    t_image = translation[chels]
    ax[i, 1].imshow(t_image, cmap="Reds_r")

plt.tight_layout()
plt.savefig('bar.png')
