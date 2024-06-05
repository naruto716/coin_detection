# Unused
from Utils.histogram import get_histogram


def adaptive_thresholding(H):
    N = sum(H)
    theta_0 = sum(i * H[i] for i in range(256)) / N  # Initial threshold

    theta_j = theta_0
    while True:
        # Separate histogram into two parts using the current threshold
        object_indices = range(int(theta_j) + 1)
        background_indices = range(int(theta_j) + 1, 256)

        N_obj = sum(H[i] for i in object_indices)
        N_bg = sum(H[i] for i in background_indices)

        if N_obj == 0 or N_bg == 0:
            break  # Avoid division by zero

        mu_obj = sum(i * H[i] for i in object_indices) / N_obj
        mu_bg = sum(i * H[i] for i in background_indices) / N_bg

        theta_j1 = 0.5 * (mu_obj + mu_bg)

        if abs(theta_j1 - theta_j) < 1e-5:
            break

        theta_j = theta_j1

    return theta_j


def get_adaptive_thresholding(pixel_array):
    histogram = get_histogram(pixel_array)
    return adaptive_thresholding(histogram)
