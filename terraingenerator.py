import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter

# Set the size of the terrain
rows = 100
cols = 100

# Create an empty 2D array to store the terrain
terrain = np.empty((rows, cols))

# Fill the array with random values between 0 and 1
terrain = np.random.rand(rows, cols)

# Apply Gaussian filter to smooth out the terrain
terrain = gaussian_filter(terrain, sigma=2)

# Define a color map
colors = [(0, "green"), (0.5, "brown"), (1, "white")]
cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Plot the terrain with the color map
plt.imshow(terrain, cmap=cmap)
plt.show()
