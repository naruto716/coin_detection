class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def connected_region_labelling(pixel_array):
    image_height = len(pixel_array)
    image_width = len(pixel_array[0])
    labeled_image = [[0 for _ in row] for row in pixel_array]
    region_dict = {}
    queue = Queue()
    label = 1
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()  # Use a set to keep track of visited pixels

    for row in range(image_height):  # Corrected loop range to iterate over image height
        for col in range(image_width):  # Corrected loop range to iterate over image width
            if pixel_array[row][col] > 0 and (row, col) not in visited:
                labeled_image[row][col] = label
                region_dict[label] = 1
                queue.enqueue((row, col))
                visited.add((row, col))  # Mark the pixel as visited

                while not queue.isEmpty():
                    pixel = queue.dequeue()
                    for dx, dy in neighbors:
                        nx, ny = pixel[0] + dx, pixel[1] + dy
                        # Check if the neighbor pixel is within the image bounds
                        if 0 <= nx < image_height and 0 <= ny < image_width:
                            if pixel_array[nx][ny] > 0 and (nx, ny) not in visited:
                                labeled_image[nx][ny] = label
                                queue.enqueue((nx, ny))
                                visited.add((nx, ny))  # Mark the neighbor pixel as visited
                                region_dict[label] += 1

                label += 1

    return labeled_image, region_dict
