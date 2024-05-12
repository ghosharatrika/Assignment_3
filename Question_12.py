"""
    This code calculates the convolution of two gaussian using
    DFT and then plots the convolved function with analytically
    obtained convolved function.
"""

import numpy as np
import matplotlib.pyplot as plt


# Defining the Gaussian function
def gaussian1(x):
    return np.exp(-x**2)


def gaussian2(x):
    return np.exp(-4*x**2)


# Defining the analytical convolution of two gaussian
def analytical_convolution(x):
    return np.sqrt(np.pi) / np.sqrt(5) * np.exp(-4*x**2/5)


# Defining the convolution function using DFT
def convolve_via_dft(g, h):
    G = np.fft.fft(g)
    H = np.fft.fft(h)
    convolved = np.fft.ifft(G * H).real
    return convolved


# Defining the range and step size for x
xmin = -5.0
xmax = 5.0
N = 500
dx = (xmax - xmin) / N
x = np.linspace(xmin, xmax, N, endpoint=False)  # Excluding endpoint to avoid redundancy

# Zero padding
f = np.pad(gaussian1(x), (0, N), mode='constant', constant_values=(0, 0))
g = np.pad(gaussian2(x), (0, N), mode='constant', constant_values=(0, 0))

# Computing the analytical convolution
convolution_analytical = analytical_convolution(x)

# Computing the convolution via DFT
convolution_dft = convolve_via_dft(f, g) * dx

# Plottting the results
plt.plot(x, f[:N], label='f(x) = exp(-$x^2$)')
plt.plot(x, g[:N], label='g(x) = exp(-$4x^2$)')
plt.plot(x, convolution_analytical, label='Analytical Convolution')
plt.plot(x, convolution_dft[N//2:3*N//2], '--', label='Convolution via DFT')
plt.xlabel('x')
plt.ylabel('Function Value')
plt.title('Convolution of g(x) and h(x)')
plt.legend()
plt.grid(True)
plt.show()
