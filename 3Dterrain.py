import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter
from mpl_toolkits.mplot3d import Axes3D

# Set the size of the terrain
rows = 100
cols = 100

# Create an empty 2D array to store the terrain
terrain = np.empty((rows, cols))

# Fill the array with random values between 0 and 1
terrain = np.random.rand(rows, cols)

# Apply Gaussian filter to smooth out the terrain
terrain = gaussian_filter(terrain, sigma=2)

# Plot the terrain in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y = np.meshgrid(range(rows), range(cols))
ax.plot_surface(x, y, terrain, cmap='terrain')

plt.show()
