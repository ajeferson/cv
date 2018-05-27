import cv2
import numpy as np


def chain_code(image, size):
    mapped = map_image(image, size)
    # for line in mapped:
    #     print line

    fp = first_pixel(mapped)
    pixel = fp
    visited = set()
    visited.add(fp)

    chain = []
    while True:
        direction, pixel = next_chain_code(mapped, pixel, size, visited)
        if pixel is None:
            break
        visited.add(pixel)
        chain.append(direction)

    print chain


    # cv2.imshow('output', mapped)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # cv2.imwrite('mapped.png', mapped)


def next_chain_code(image, cp, s, visited):
    n = image.shape[0]
    if cp[1] + s < n and image[cp[0], cp[1] + s] != 0 and not (cp[0], cp[1] + s) in visited:
        return 0, (cp[0], cp[1] + s)
    elif cp[0] - s < n and image[cp[0] - s, cp[1]] != 0 and not (cp[0] - s, cp[1]) in visited:
        return 2, (cp[0] - s, cp[1])
    elif cp[1] - s < n and image[cp[0], cp[1] - s] != 0 and not (cp[0], cp[1] - s) in visited:
        return 4, (cp[0], cp[1] - s)
    elif cp[0] + s < n and image[cp[0] + s, cp[1]] != 0 and not (image[cp[0] + s, cp[1]]) in visited:
        return 6, (cp[0] + s, cp[1])
    elif cp[0] - s < n and cp[1] + s < n and image[cp[0] - s, cp[1] + s] != 0  and not (cp[0] - s, cp[1] + s) in visited:
        return 1, (cp[0] - s, cp[1] + s)
    elif cp[0] - s < n and cp[1] - s < n and image[cp[0] - s, cp[1] - s] != 0and not (cp[0] - s, cp[1] - s) in visited:
        return 3, (cp[0] - s, cp[1] - s)
    elif cp[0] + s < n and cp[1] - s < n and image[cp[0] + s, cp[1] - s] != 0 and not (cp[0] + s, cp[1] - s) in visited:
        return 5, (cp[0] + s, cp[1] - s)
    elif cp[0] + s < n and cp[1] + s < n and image[cp[0] + s, cp[1] + s] != 0 and not (cp[0] + s, cp[1] + s) in visited:
        return 7, (cp[0] + s, cp[1] + s)
    return None, None


def map_image(image, size):
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

    return output


def first_pixel(image):
    n = image.shape[0]
    for i in range(n):
        for j in range(n):
            if image[i, j] != 0:
                return i, j


img = cv2.imread('images/6/0.png', 0)
chain_code(img, 4)