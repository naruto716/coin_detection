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


def find_valid_region_bounds(image):
    region_dict = find_region_bounds(image)
    valid_regions = {}
    value = 1

    for region_id, region_bounds in region_dict.items():
        min_x, max_x = region_bounds['min_x'], region_bounds['max_x']
        min_y, max_y = region_bounds['min_y'], region_bounds['max_y']

        width = max_x - min_x + 1
        height = max_y - min_y + 1

        # Check if the size of the box is within valid range
        if width >= 100 and width <= 400 and height >= 100 and height <= 400:
            # Check if the ratio of width/height is close to 1
            aspect_ratio = width / height
            if 0.8 <= aspect_ratio <= 1.2:
                valid_regions[value] = {
                    'min_x': min_x, 'max_x': max_x,
                    'min_y': min_y, 'max_y': max_y
                }
                value += 1

    return valid_regions, value - 1
