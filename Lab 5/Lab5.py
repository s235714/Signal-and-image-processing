import numpy as np
import matplotlib.pyplot as plt

# https://gist.github.com/xehivs/786d9d1d3aabe3d6ae4a137e17f740a5

points = np.array([
	               [0,0],
	               [1,0],
	               [1,1],
	               [0,1],
                   [0,0]
                  ])
ones = np.ones((5,1))
A = np.concatenate((points, ones), axis = 1)
print(A)

T = {
    '1':
        np.array([
	       [1,0,0],
	       [0,1,0],
	       [0,0,1],
        ]),
    '2':
        np.array([
	       [1,0, .5],
	       [0,1, .5],
	       [0,0,1  ]
        ]),
    '3':
        np.array([
	       [-1,0,0],
	       [ 0,1,0],
	       [ 0,0,1]
        ]),
    '4':
        np.array([
	       [1, 0,0],
	       [0,-1,0],
	       [0, 0,1]
        ]),
    '5':
        np.array([
	       [2,0,0],
	       [0,1,0],
	       [0,0,1]
        ]),
    '6':
        np.array([
	       [1,0,0],
	       [0,2,0],
	       [0,0,1]
        ]),
    '7':
        np.array([
	       [np.cos(np.pi/4), -np.sin(np.pi/4),0],
	       [np.sin(np.pi/4),  np.cos(np.pi/4),0],
	       [0         ,0           ,1]
        ]),
    '8':
        np.array([
	       [1, .5,0],
	       [0,1  ,0],
	       [0,0  ,1]
        ]),
    '9':
        np.array([
	       [1, .5,0],
	       [0,1  ,0],
	       [0,0  ,1]
        ])
}


fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(10, 10))

for x, item in enumerate(T.items()):
    name, t = item
    Z = A @ t.T

    axs[x // 3, x % 3].plot(A[:,0],A[:,1], 'c')
    axs[x // 3, x % 3].plot(Z[:,0],Z[:,1], 'm')

plt.savefig('obraz.png')
