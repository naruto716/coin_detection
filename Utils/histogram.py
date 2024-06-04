def get_histogram(px_array_grey):
    histogram = [0] * 256
    for row in px_array_grey:
        for pixel in row:
            histogram[round(pixel)] += 1
    return histogram


def get_cumulative_histogram(histogram):
    cumulative_histogram = [0] * 256
    cumulative_histogram[0] = histogram[0]
    for i in range(1, 256):
        cumulative_histogram[i] = cumulative_histogram[i - 1] + histogram[i]
    return cumulative_histogram
