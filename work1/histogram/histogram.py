import cv2
import numpy as np
import matplotlib.pyplot as plt


def histogram(filename):
    result = np.zeros(256)
    image = cv2.imread(filename, 0)
    height, width = image.shape
    for i in range(height):
        for j in range(width):
            result[image[i, j]] += 1

    plt.bar(range(256), result, color='black')
    plt.show()


histogram('cells.jpg')

