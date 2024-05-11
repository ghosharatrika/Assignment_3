"""
   This code calculates the fourier transform of constant function
   using numpy.fft.fft() and then plots the solution obatained along 
   with the constant function.
"""

xmin = -10.0
xmax = 10.0
n = 256
dx = (xmax - xmin) / n

const_fn = 5 * np.ones(n)  # Defining the constant function

xp = np.linspace(xmin, xmax, n)
kq = np.fft.fftfreq(n, d=dx) * 2 * np.pi

# Calculating the factor for proper normalization of the fourier transformed function
factor = np.real(dx * np.sqrt(n / (2 * np.pi)) * np.exp(-j * kq * xmin))

# Calculating the fft of constant function with proper normalization
dft = np.fft.fft(const_fn, norm='ortho')
num_ft = dft * factor  # Multiplying by proper factor

# Plotting the results
plt.subplot(1, 2, 1)
plt.plot(xp, const_fn, label='f(x) = 5.0')
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.title('Constant Function')
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(kq, abs(num_ft), color='blue', label="numerical FT")
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.title('Fourier Transform')
plt.legend()
plt.grid()

plt.show()
