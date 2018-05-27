import cv2
import numpy as np


def moore_boundary(image):
    fp = first_pixel(image)

    path = boundary(fp, image)
    if path is None:
        return

    output = np.zeros(image.shape)
    for index in path:
        output[index] = 255

    return output, path


def first_pixel(image):
    n = image.shape[0]
    for i in range(n):
        for j in range(n):
            if image[i, j] != 0:
                return i, j


def boundary(start, image):
    b0 = start
    c0 = (start[0], start[1] - 1)

    b = [b0]

    bi, ci = find_next_neighbor(image, b0, c0)

    # Error
    if bi is None:
        return None

    b.append(bi)

    while True:
        bi, ci = find_next_neighbor(image, bi, ci)

        if bi is None:
            return None

        if bi == b[0]:
            return b
        b.append(bi)


def find_next_neighbor(image, bi, ci):
    diffs = [
        (0, -1),  # Left
        (-1, -1),  # Top Left
        (-1, 0),  # Top
        (-1, 1),  # Top Right
        (0, 1),  # Right
        (1, 1),  # Bottom Right
        (1, 0),  # Bottom
        (1, -1)  # Bottom Left
    ]

    # Find index
    res = (ci[0] - bi[0], ci[1] - bi[1])
    index = -1
    for i in range(len(diffs)):
        if diffs[i] == res:
            index = i
            break

    # ci and bi are not neighbors
    if index < 0:
        return

    c = 0
    while c < 9:
        neighbor = (bi[0] + diffs[index][0], bi[1] + diffs[index][1])
        if image[neighbor] != 0:
            previous = (bi[0] + diffs[index - 1][0], bi[1] + diffs[index - 1][1])
            return neighbor, previous
        index += 1
        if index == len(diffs):
            index = 0
        c += 1

    return None, None

