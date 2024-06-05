def median_filter(pixel_array):
    image_height = len(pixel_array)
    image_width = len(pixel_array[0])

    def get_extended_array():
        new_pixel_array = [row[:] for row in pixel_array]
        for r in range(len(new_pixel_array)):
            new_pixel_array[r].insert(0, 0)
            new_pixel_array[r].append(0)
        new_pixel_array.insert(0, [0 for _ in range(image_width + 2)])
        new_pixel_array.append([0 for _ in range(image_width + 2)])
        return new_pixel_array

    extended_array = get_extended_array()
    result_array = [[0 for _ in range(image_width)] for _ in range(image_height)]  # Initialize the array

    for row in range(1, len(extended_array) - 1):
        for col in range(1, len(extended_array[row]) - 1):
            value_array = []
            for i in range(-1, 1 + 1):
                for j in range(-1, 1 + 1):
                    pixel_value = extended_array[row + i][col + j]
                    value_array.append(pixel_value)
            value_array.sort()
            length = len(value_array)
            if length % 2 == 1:
                result_array[row - 1][col - 1] = value_array[length // 2]
            else:
                result_array[row - 1][col - 1] = (value_array[length // 2 - 1] + value_array[length // 2]) / 2

    return result_array

def apply_median(pixel_array, times=3):
    result_array = pixel_array
    for i in range(times):
        result_array = median_filter(result_array)
    return result_array