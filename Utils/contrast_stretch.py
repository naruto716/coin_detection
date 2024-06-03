def get_histogram(px_array_grey):
    histogram = [0] * 256
    for row in px_array_grey:
        for pixel in row:
            histogram[pixel] += 1
    return histogram


def get_cumulative_histogram(histogram):
    cumulative_histogram = [0] * 256
    cumulative_histogram[0] = histogram[0]
    for i in range(1, 256):
        cumulative_histogram[i] = cumulative_histogram[i - 1] + histogram[i]
    return cumulative_histogram


def find_percentile_value(cumulative_histogram, percentile_alpha, percentile_beta):
    total_pixels = cumulative_histogram[255]
    alpha_percent_pixels = total_pixels * percentile_alpha / 100
    beta_percent_pixels = total_pixels * percentile_beta / 100

    p_alpha = -1
    for pixel, value in enumerate(cumulative_histogram):
        if value > alpha_percent_pixels:
            p_alpha = pixel
            break

    p_beta = -1
    for i, value in enumerate(cumulative_histogram[::-1]):
        if value < beta_percent_pixels:
            p_beta = 255 - i
            break

    return p_alpha, p_beta


def contrast_stretch(px_array_grey, alpha=5, beta=95):
    histogram = get_histogram(px_array_grey)
    cumulative_histogram = get_cumulative_histogram(histogram)
    p_alpha, p_beta = find_percentile_value(cumulative_histogram, alpha, beta)
    px_stretched_array_grey = [[0 for _ in row] for row in px_array_grey]
    for i in range(len(px_array_grey)):
        for j in range(len(px_array_grey[i])):
            pixel = px_array_grey[i][j]
            if pixel < p_alpha:
                px_stretched_array_grey[i][j] = 0
            elif pixel > p_beta:
                px_stretched_array_grey[i][j] = 255
            else:
                px_stretched_array_grey[i][j] = (pixel - p_alpha) * (255 / (p_beta - p_alpha))

    return px_stretched_array_grey
