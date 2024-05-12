"""
    This code calculates DFT of n numbers using two methods: direct DFT and 
    using numpy.fft.fft() and then compares the time taken to calculate dft 
    for a range of values for n, and plots the time taken.
"""

import numpy as np
import time
import matplotlib.pyplot as plt

j = complex(0, 1)


def direct_dft(num):
    n = len(num)
    p = np.arange(n)
    q = p.reshape((n, 1))
    fact = np.exp(-j * 2 * np.pi * p * q / n)
    return np.dot(fact, num) / np.sqrt(n)


# Function to compute DFT using numpy.fft.fft
def numpy_fft_dft(num):
    return np.fft.fft(num, norm='ortho')


# Function to measure time taken by each method for different values of n
def measure_time(n_values):
    direct_dft_times = []
    numpy_fft_times = []
    for n in n_values:
        numbers = np.random.rand(n)  # Random number generator is used to generate n numbers
        start_time = time.time()
        direct_dft(numbers)

        direct_dft_time = time.time() - start_time
        direct_dft_times.append(direct_dft_time)

        start_time = time.time()
        numpy_fft_dft(numbers)
        numpy_fft_time = time.time() - start_time
        numpy_fft_times.append(numpy_fft_time)

    return direct_dft_times, numpy_fft_times


# Range of values for n
n_values = range(4, 101)

direct_dft_time, numpy_fft_time = measure_time(n_values)

# Plotting
plt.plot(n_values, direct_dft_time, label='Direct DFT')
plt.plot(n_values, numpy_fft_time, label='Numpy FFT')
plt.xlabel('Number of elements (n)')
plt.ylabel('Time taken to compute DFT (seconds)')
plt.title('Comparison of Direct DFT vs Numpy FFT')
plt.legend()
plt.grid()
plt.show()
