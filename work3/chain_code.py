import cv2
import numpy as np


def chain_code(image, m):
    mapped = map_image(image, m, False)

    fp = first_pixel(mapped)
    contours = boundary(fp, mapped, m)

    # Build the chain
    list_chain = build_chain(contours, m)
    str_chain = [str(c) for c in list_chain]
    chain = ''.join(str_chain)

    return chain


def build_chain(contours, m):
    chain = []
    c = contours[:]  # Copy the list
    c.append(c[0])  # Circular list

    for i in range(1, len(c)):
        next_dir = direction(c[i - 1], c[i], m)
        chain.append(next_dir)
    return chain


def direction(origin, destination, m):
    diffs = {
        (0, m): 0,
        (-m, m): 1,
        (-m, 0): 2,
        (-m, -m): 3,
        (0, -m): 4,
        (m, -m): 5,
        (m, 0): 6,
        (m, m): 7
    }
    res = (destination[0] - origin[0], destination[1] - origin[1])
    return diffs[res]


def boundary(start, image, m):
    b0 = start
    c0 = (start[0], start[1] - m)

    b = [b0]

    bi, ci = find_next_neighbor(image, b0, c0, m)

    # Error
    if bi is None:
        return None

    b.append(bi)

    while True:
        bi, ci = find_next_neighbor(image, bi, ci, m)

        if bi is None:
            return None

        if bi == b[0]:
            return b
        b.append(bi)


def find_next_neighbor(image, bi, ci, m):
    diffs = [
        (0, -m),   # Left
        (-m, -m),  # Top Left
        (-m, 0),   # Top
        (-m, m),   # Top Right
        (0, m),    # Right
        (m, m),    # Bottom Right
        (m, 0),    # Bottom
        (m, -m)    # Bottom Left
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
    n = image.shape[0]
    while c < 9:
        neighbor = (bi[0] + diffs[index][0], bi[1] + diffs[index][1])
        if neighbor[0] < n and neighbor[1] < n and image[neighbor] != 0:
            previous = (bi[0] + diffs[index - 1][0], bi[1] + diffs[index - 1][1])
            return neighbor, previous
        index += 1
        if index == len(diffs):
            index = 0
        c += 1

    return None, None


def map_image(image, size, write):
    n = image.shape[0]
    guides = [i for i in range(0, n, size)]

    output = np.zeros(image.shape)
    for i in range(n):
        for j in range(n):
            if image[i, j] != 0:
                ik = n
                xk = 0
                while xk < len(guides) and abs(i - guides[xk]) <= ik:
                    ik = abs(i - guides[xk])
                    xk += 1

                jk = n
                yk = 0
                while yk < len(guides) and abs(j - guides[yk]) <= jk:
                    jk = abs(j - guides[yk])
                    yk += 1

                xk -= 1
                yk -= 1
                output[guides[xk], guides[yk]] = 255

    if write:
        cv2.imwrite('mapped.png', output)

    return output


def first_pixel(image):
    n = image.shape[0]
    for i in range(n):
        for j in range(n):
            if image[i, j] != 0:
                return i, j
