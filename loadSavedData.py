import matplotlib.pyplot as plt
import numpy as np

# open data
npzfile = np.load('xaPre_height_velocity_neutral.npz')
z = npzfile['y']
U = npzfile['x']

# plot
plt.plot(U, z)
plt.grid
plt.show()