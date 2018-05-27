import cv2
from moore import moore_boundary
from chain_code import chain_code


def max_diameter(image, d):
    n = image.shape[0]
    max_dia = 0
    max_i = -1
    for i in range(n):
        dia = diameter(image, i, d)
        if dia is not None and dia > max_dia:
            max_dia = dia
            max_i = i
    return max_dia, max_i


def max_diameter_horizontal(image):
    return max_diameter(image, 0)


def max_diameter_vertical(image):
    return max_diameter(image, 1)


def diameter(image, i, d):
    n = image.shape[0]

    def pixel(pi, pj, pd):
        if pd == 0:
            return image[pi, pj]
        return image[pj, pi]

    j = 0
    while j < n and pixel(i, j, d) == 0:
        j += 1
    if j >= n:
        return None
    first = j

    j = image.shape[0] - 1
    while j >= 0 and pixel(i, j, d) == 0:
        j -= 1
    if j < 0:
        return None
    last = j

    return last - first + 1


def eccentricity(image):
    hor = max_diameter_horizontal(image)[0]
    ver = max_diameter_vertical(image)[0]
    return float(hor) / float(ver)


def boundary_length(path):
    return len(path)


def compact_chain(chain):
    if len(chain) == 0:
        return ''
    compacted = chain[0]
    for i in range(1, len(chain)):
        if chain[i - 1] != chain[i]:
            compacted += chain[i]
    return compacted


def count_directions(chain, dirs):
    count = 0
    for c in chain:
        if c in dirs:
            count += 1
    return count


def slopes(chain):
    compacted = compact_chain(chain)
    return count_directions(compacted, '1357')


def direction_sum(chain):
    compacted = compact_chain(chain)
    s = 0
    for c in compacted:
        s += int(c)
    return s

img = cv2.imread('images/0/0.png', 0)
output, path = moore_boundary(img)
print path
chain = chain_code(img, 4)
print chain
print direction_sum(chain)