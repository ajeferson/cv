import cv2
import numpy as np
import matplotlib.pyplot as plt


def equalization(filename):

    result = np.zeros(256)
    sk = np.zeros(256)

    image = cv2.imread(filename, 0)
    output = cv2.imread(filename, 0)

    height, width = image.shape
    n = height * width

    # Calculate the probabilities
    for i in range(height):
        for j in range(width):
            result[image[i, j]] += 1

    # Calculate sk
    accumulate = 0
    for i in range(256):
        accumulate += result[i] / n
        sk[i] = round(255 * accumulate, 0)

    # Replace values
    for i in range(height):
        for j in range(width):
            output[i, j] = sk[image[i, j]]

    # Display image
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save to file
    cv2.imwrite('equalization_%s' % filename, output)

    plt.bar(range(256), sk, color='black')
    plt.show()


equalization('cells.jpg')

