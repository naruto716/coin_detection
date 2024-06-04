def create_init_array(image_width, image_height):
    return [[0 for _ in range(image_width)] for _ in range(image_height)]


def dilate(pixel_array):
    image_height = len(pixel_array)
    image_width = len(pixel_array[0])
    # Create an empty greyscale array for the output image
    dilated_image = create_init_array(image_width, image_height)

    # Add zero padding around the original image
    padded_image = create_init_array(image_width + 4, image_height + 4)
    for y in range(image_height):
        for x in range(image_width):
            padded_image[y + 2][x + 2] = pixel_array[y][x]

    structuring_element = [[0, 0, 1, 0, 0],
                           [0, 1, 1, 1, 0],
                           [1, 1, 1, 1, 1],
                           [0, 1, 1, 1, 0],
                           [0, 0, 1, 0, 0]]

    for row in range(2, image_height + 2):
        for col in range(2, image_width + 2):
            for i in range(-2, 2 + 1):
                for j in range(-2, 2 + 1):
                    if structuring_element[i + 2][j + 2] and padded_image[row + i][col + j]:
                        dilated_image[row - 2][col - 2] = 1
                        break
                if dilated_image[row - 2][col - 2] == 1:
                    break

    return dilated_image


def erode(pixel_array):
    image_height = len(pixel_array)
    image_width = len(pixel_array[0])
    # Create an empty greyscale array for the output image
    eroded_image = create_init_array(image_width, image_height)

    # Add zero padding around the original image
    padded_image = create_init_array(image_width + 4, image_height + 4)
    for y in range(image_height):
        for x in range(image_width):
            padded_image[y + 2][x + 2] = pixel_array[y][x]

    # Define the 5x5 structuring element
    structuring_element = [[0, 0, 1, 0, 0],
                           [0, 1, 1, 1, 0],
                           [1, 1, 1, 1, 1],
                           [0, 1, 1, 1, 0],
                           [0, 0, 1, 0, 0]]

    for row in range(2, image_height + 2):
        for col in range(2, image_width + 2):
            eroded_image[row - 2][col - 2] = 1
            for i in range(-2, 2 + 1):
                for j in range(-2, 2 + 1):
                    if structuring_element[i + 2][j + 2] and padded_image[row + i][col + j] == 0:
                        eroded_image[row - 2][col - 2] = 0
                        break
                if eroded_image[row - 2][col - 2] == 0:
                    break

    return eroded_image
