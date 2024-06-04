import matplotlib.pyplot as plt


def plot_histogram(histogram):
    plt.figure(figsize=(10, 6))
    plt.plot(histogram, color='black')
    plt.title('Greyscale Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.grid(True)
    plt.show()
