"""
   This code calculates the convolution of a box function with itself
   using DFT. Then it plots the convolved result with the box function.
"""

import numpy as np
import matplotlib.pyplot as plt


# Defining the box function
def box_function(x):
    return np.where(np.logical_and(x >= -1, x <= 1), 1, 0)


# Defining the convolution function using DFT
def convolve_via_dft(g, h):
    G = np.fft.fft(g)
    H = np.fft.fft(h)
    convolved = np.fft.ifft(G * H).real
    return convolved


# Defining the range and step size for x
xmin = -4.0
xmax = 4.0
N = 256
dx = (xmax - xmin) / N
x = np.arange(xmin, xmax, dx)

# Zero padding
box1 = np.pad(box_function(x), (0, N), mode='constant', constant_values=(0, 0))
box2 = np.pad(box_function(x), (0, N), mode='constant', constant_values=(0, 0))

# Computing the convolution of the box function with itself
conv_box2 = convolve_via_dft(box1, box2) * dx
# Plotting the box function and the convolution result
plt.plot(x, box_function(x), label='Box Function $f(x)$', color='blue')
plt.plot(x, conv_box2[N//2:3*N//2], '--', label='Convolution via DFT', color='red')
plt.xlabel('x')
plt.ylabel('f*f')
plt.title('Convolution of Box Function')
plt.legend()
plt.grid(True)
plt.show()
