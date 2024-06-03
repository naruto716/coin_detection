def border_ignore_filter(pixel_array, kernel):
    image_height = len(pixel_array)
    image_width = len(pixel_array[0])
    result_array = [[0 for _ in range(image_width)] for _ in range(image_height)]  # Initialize the array

    for row in range(1, image_height - 1):
        for col in range(1, image_width - 1):
            accumulator = 0
            for i in range(-1, 1 + 1):  # row
                for j in range(-1, 1 + 1):  # column
                    image_value = pixel_array[row + i][col + j]
                    kernel_value = kernel[i + 1][j + 1]  # +1 to shift
                    accumulator += image_value * kernel_value
            result_array[row][col] = accumulator

    return result_array


def edge_filter_x(px_stretched_grey):
    scharr_x_kernel = [[3 / 32, 0, -3 / 32],
                       [10 / 32, 0, -10 / 32],
                       [3 / 32, 0, -3 / 32]]
    return border_ignore_filter(px_stretched_grey, scharr_x_kernel)


def edge_filter_y(px_stretched_grey):
    scharr_x_kernel = [[3 / 32, 10 / 32, 3 / 32],
                       [0, 0, 0],
                       [-3 / 32, -10 / 32, -3 / 32]]
    return border_ignore_filter(px_stretched_grey, scharr_x_kernel)


def edge_map(px_stretched_grey):
    gx = edge_filter_x(px_stretched_grey)
    gy = edge_filter_y(px_stretched_grey)
    gm = [[abs(gx[i][j]) + abs(gy[i][j]) for j in range(1, len(gx[i]))] for i in range(1, len(gx))]
    return gm
