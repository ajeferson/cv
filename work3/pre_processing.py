import cv2
import numpy as np

number_count = {}
for i in range(10):
    number_count[i] = -1


class Number:

    def __init__(self, n, array):
        self.number = n
        self.image = np.array(array, dtype = np.uint8)

    def __str__(self):
        s = ''
        for line in self.image:
            s += "%s\n" % str(line)
        return s

    def show(self):
        title = "Output: %d" % self.number
        cv2.imshow(title, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save(self):
        count = number_count[self.number] + 1
        dir = "images/%d" % self.number
        filename = "%s/%d.png" % (dir, count)
        number_count[self.number] = count
        cv2.imwrite(filename, self.image)


def map_pixel(value):
    if value == 0:
        return 0
    return 255


def process_line(line, dimension):
    post = line.split()
    post = [int(n) for n in post]
    number = post.pop()
    post = [map_pixel(n) for n in post]
    matrix = []
    for i in range(dimension):
        temp = []
        for j in range(i*dimension, (i+1)*dimension):
            temp.append(post[j])
        matrix.append(temp)
    return Number(number, matrix)


def read_numbers(n_lines, dimension):
    array = []
    with open('numbers.txt', 'r') as file_numbers:
        for line in file_numbers:
            post = process_line(line, dimension)
            array.append(post)
            if 0 < n_lines <= len(array):
                return array
    return array


def save_numbers(nnumbers):
    for number in nnumbers:
        number.save()


numbers = read_numbers(-1, 35)
save_numbers(numbers)

