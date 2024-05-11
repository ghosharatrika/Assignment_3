"""
    This code calculates the Fourier transform of sinc function using
    DFT and then properly normalizes it. Then it plots the original
    function as well as numerically obtained FT along with analytical 
    fourier transform.
"""

import numpy as np
import matplotlib.pyplot as plt

j = complex(0, 1)


# Defining the sinc function
def func(x):
    if x != 0:
        return np.sin(x) / x
    else:
        return 1


# Analytical fourier transform of sinc function
def ft_func(k):
    if -1 <= k <= 1:
        return np.sqrt(np.pi / 2)
    else:
        return 0


xmin = -50.0
xmax = 50.0
n = 128
dx = (xmax - xmin) / n

xp = np.linspace(xmin, xmax, n)
kq = np.fft.fftfreq(n, d=dx) * 2 * np.pi
dft = np.zeros(n)
fn = np.zeros(n)
ana_ft = np.zeros(n)
factor = np.zeros(n)

for i in range(n):
    fn[i] = func(xp[i])
    ana_ft[i] = ft_func(kq[i])
    # Calculating factor to convert dft to FT
    factor[i] = np.real(dx * np.sqrt(n / (2 * np.pi)) * np.exp(-j * kq[i] * xmin))

# Calculating the fft of sinc function with proper normalization
dft = np.fft.fft(fn, norm='ortho')
num_ft = dft * factor  # Multiplying by proper factor

# Plotting the results
plt.subplot(1, 2, 1)
plt.plot(xp, fn, label='Sinc function')
plt.scatter(xp, fn, color='black')
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.title('Sinc Function')
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(kq, abs(num_ft), color='red', label="numerical FT")
plt.plot(kq, ana_ft, color='blue', label='Analytical FT')
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.title('Fourier Transform')
plt.legend()
plt.grid()

plt.show()
