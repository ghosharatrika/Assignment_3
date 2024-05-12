"""
    This code uses numpy.fft.fft2() to calculate the fourier
    transform of a 2D gaussian function and plot the result
    obtained along with the analytically obtained fourier
    transformed function.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

j = complex(0, 1)


# Define the Gaussian function
def gaussian(x, y):
    return np.exp(-(x**2 + y**2))


# Defining the range of x and y values and creating a grid
xmin = -20.0
xmax = 20.0
n = 256
dx = (xmax - xmin) / n
dy = dx
x = np.linspace(xmin, xmax, n, endpoint=False)
y = np.linspace(xmin, xmax, n, endpoint=False)  # x and y have the same range from (-20,20)
X, Y = np.meshgrid(x, y)

# Computing the Gaussian function values on the grid
f = gaussian(X, Y)


# Analytical Fourier Transform of Gaussian
def gaussian_FT(kx, ky):
    return np.exp(-(kx**2 + ky**2) / 4) / 2


# Defining the range of kx and ky values
kx = np.fft.fftfreq(n, d=dx) * 2 * np.pi
ky = np.fft.fftfreq(n, d=dy) * 2 * np.pi
KX, KY = np.meshgrid(kx, ky)  # Creating grid in fourier space

# Calculating the proper factor to calculate the fourier transform from DFT obtained
factor = np.real(dx*dy * 1 / (2 * np.pi)) * np.exp(- j * (kx + ky) * xmin)  # Since xmin and ymin is same
F = np.fft.fft2(f) * factor  # Computing the Fourier transform using numpy.fft.fft2

# Computing the analytical Fourier transform of the Gaussian function
F_analytical = gaussian_FT(KX, KY)

# Plotting the result
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(KX, KY, np.abs(F), cmap='viridis')
ax1.set_title('Numerical Fourier Transform')
ax1.set_xlabel('$k_x$')
ax1.set_ylabel('$k_y$')
ax1.set_zlabel('F($k_x$,$k_y$)')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(KX, KY, np.abs(F_analytical), cmap='viridis')
ax2.set_title('Analytical Fourier Transform')
ax2.set_xlabel('$k_x$')
ax2.set_ylabel('$k_y$')
ax2.set_zlabel('F_analytical')

plt.tight_layout()
plt.show()
