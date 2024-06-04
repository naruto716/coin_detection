def mean_filter(pixel_array):
    result_array = [[0.0 for _ in row] for row in pixel_array]

    for row in range(2, len(pixel_array) - 2):
        for col in range(2, len(pixel_array[row]) - 2):
            accumulator = 0
            for i in range(-2, 2 + 1):
                for j in range(-2, 2 + 1):
                    accumulator += pixel_array[row + i][col + j]
            result_array[row][col] = abs(accumulator / 25)

    return result_array


def image_blur(pixel_array, times=3):
    result_array = pixel_array
    for i in range(times):
        result_array = mean_filter(result_array)
    return result_array
