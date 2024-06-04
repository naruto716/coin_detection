def find_region_bounds(image):
    region_dict = {}

    for y, row in enumerate(image):
        for x, value in enumerate(row):
            if value != 0:  # Ignore background
                if value not in region_dict:
                    region_dict[value] = {
                        'min_x': x, 'max_x': x,
                        'min_y': y, 'max_y': y
                    }
                else:
                    region_dict[value]['min_x'] = min(region_dict[value]['min_x'], x)
                    region_dict[value]['max_x'] = max(region_dict[value]['max_x'], x)
                    region_dict[value]['min_y'] = min(region_dict[value]['min_y'], y)
                    region_dict[value]['max_y'] = max(region_dict[value]['max_y'], y)

    return region_dict