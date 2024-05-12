"""
   This code calculates and plots the power spectrum by reading some time
   series measurement and using periodogram. It also plots the histogram of 
   power spectrum by binning the power spectrum in ten k bins.
"""

import numpy as np
import matplotlib.pyplot as plt

# Reading data from file
data = np.loadtxt('noise.txt')

# Plotting measurements as a function of time
plt.plot(data, label='Measurements')
plt.xlabel('Time')
plt.ylabel('Data value')
plt.title('Measurements')
plt.legend()
plt.grid(True)
plt.show()

# Computing and plotting DFT of the measurement
dft = np.fft.fftshift(np.fft.fft(data, norm='ortho'))
freq = np.fft.fftshift(np.fft.fftfreq(len(data)))
# Plotting DFT
plt.plot(freq, abs(dft), label='DFT')
plt.xlabel('Frequency (k)')
plt.ylabel('Magnitude')
plt.title('Discrete Fourier Transform')
plt.legend()
plt.grid(True)
plt.show()

# Computing power spectrum using periodogram
power_spectrum = np.abs(dft) ** 2
# Plotting power spectrum
plt.plot(freq, power_spectrum, label='Power Spectrum')
plt.xlabel('Frequency (k)')
plt.ylabel('|F(k)|$^2$')
plt.title('Power Spectrum')
plt.legend()
plt.grid(True)
plt.show()

# Binning the power spectrum into ten k bins
num_bins = 10
bin_edges = np.linspace(freq.min(), freq.max(), num_bins + 1)
binned_power_spectrum = []

"""
    In this loop, first the indices of the frequency values that fall within the bin's frequency range
    are determined. Then the power spectrum corresponding to those frequencies are determined and their 
    mean is stored in the bins.
"""
for i in range(num_bins):
    bin_indices = np.where(np.logical_and(freq >= bin_edges[i], freq < bin_edges[i + 1]))
    bin_power_spectrum = power_spectrum[bin_indices]
    bin_mean = np.mean(bin_power_spectrum)
    binned_power_spectrum.append(bin_mean)
  
# Plotting the binned power spectrum as histogram
mean_freq = (bin_edges[:-1] + bin_edges[1:]) / 2  # Calculating mean frequency for each bin
plt.hist(mean_freq, bins=bin_edges, weights=binned_power_spectrum, color='skyblue', edgecolor='black')
plt.xlabel('Frequency(k)')
plt.ylabel('Power')
plt.title('Binned Power Spectrum')
plt.grid(True)
plt.show()
