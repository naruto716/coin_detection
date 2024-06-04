def threshold_image(pixel_array, threshold=22):
    result_array = [[0 for _ in row] for row in pixel_array]
    for i in range(len(pixel_array)):
        for j in range(len(pixel_array[i])):
            if pixel_array[i][j] < threshold:
                result_array[i][j] = 0
            else:
                result_array[i][j] = 255
    return result_array
