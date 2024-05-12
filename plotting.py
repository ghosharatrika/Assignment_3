"""
    This code plots from the two input data file by first
    sorting the data in increasing order of the first column.
"""

import matplotlib.pyplot as plt


# Reading data from the files
def read_file(filename):
    x_values = []
    y_values = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            x_values.append(x)
            y_values.append(y)
    # Sorting the data based on the first column values
    sorted_indices = sorted(range(len(x_values)), key=lambda i: x_values[i])
    x_values = [x_values[i] for i in sorted_indices]
    y_values = [y_values[i] for i in sorted_indices]
    return x_values, y_values


# Plotting data
def plot_data(x, y1, y2):
    plt.plot(x, y1, label='GSL solution', color='Red')
    plt.plot(x, y2, '--', label='Analytical Solution', color='Black')
    plt.xlabel('k')
    plt.ylabel('F(k)')
    plt.title('Fourier transform of Sinc function(GSL)')
    plt.xlim(-5, 5)
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    # Assuming the files contain numerical data separated by newline characters
    file1 = 'box1'  # Filename for file containing the numerical ft
    file2 = 'box2'  # Filename for file containing the analytical ft

    x1, y1 = read_file(file1)
    x2, y2 = read_file(file2)

    # Plotting the data from both files
    plot_data(x1, y1, y2)
