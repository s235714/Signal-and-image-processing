import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import rectangle
from skimage.transform import rotate
from scipy.signal import convolve2d, medfilt

# https://gist.github.com/xehivs/a176f923fffed0a371e3b5d319797dc1
# https://pastebin.com/aCM83AGP

entry_img = np.zeros(shape = (256, 256)).astype(float)
entry_img[rectangle(start = (32,32), end = (92,92))] = 1.0
entry_img[rectangle(start = (92,92), end = (128,128))] = 1.0
entry_img[rectangle(start = (128,128), end = (144,144))] = 1.0

fig, axs = plt.subplots(nrows=3, ncols=2)


angle = np.random.randint(-20, 20)
rot_img = rotate(entry_img, angle)


angles = np.linspace(-30, 30, 50)
abssums_s1 = np.zeros(50)
abssums_s2 = np.zeros(50)

s1 = np.array([[-1, 0, 1],[-2, 0, 2],[-1,0,1]])
s3 = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

for x, a in enumerate (angles):
    axs[0][0].imshow(entry_img, cmap = 'binary')
    axs[0][0].set_title('Original image')

    axs[0][1].imshow(rot_img, cmap = 'binary')
    axs[0][1].set_title('Transformed image')

    current_img = rotate(rot_img, a)
    axs[1][0].imshow(current_img, cmap = 'binary')
    axs[1][0].set_title('Current rotation')

    con_s1 = convolve2d(current_img, s1)
    con_s3 = convolve2d(current_img, s3)
    axs[1][1].imshow(con_s1, cmap = 'gray')
    axs[1][1].set_title('S1 convolved image')

    abssums_s1[x] = np.sum(np.abs(con_s1))
    abssums_s2[x] = np.sum(np.abs(con_s3))
    axs[2][0].plot(angles[:x], abssums_s1[:x])
    axs[2][0].plot(angles[:x], abssums_s2[:x])

    axs[2][0].set_title('Plot of measures')

    axs[2][1].imshow(con_s3, cmap = 'gray')
    axs[2][1].set_title('S3 convolved image')

min_s1 = abssums_s1.argmin()
best_angle_s1 = angles[min_s1]

min_s3 = abssums_s2.argmin()
best_angle_s2 = angles[min_s1]

best_angle = (best_angle_s1 + best_angle_s2)/2

final_img = rotate(rot_img, best_angle)

stacked = np.stack([entry_img, final_img, rot_img], axis=-1)
plt.imsave('baz.png', final_img)
plt.imsave('bar.png', stacked)

plt.tight_layout()
plt.savefig('obraz.png')
