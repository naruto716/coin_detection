def convert_to_greyscale(px_array_r, px_array_g, px_array_b):
    px_array_grey = []
    for i in range(len(px_array_r)):
        px_array_grey.append([round(0.3 * px_array_r[i][j] + 0.6 * px_array_g[i][j] + 0.1 * px_array_b[i][j]) for j in
                              range(len(px_array_r[i]))])
    return px_array_grey
