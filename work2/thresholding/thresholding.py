import numpy as np
import matplotlib.pyplot as plt
import cv2


def histogram(image, t):

    result = np.zeros(256)
    height, width = image.shape

    for i in range(height):
        for j in range(width):
            result[image[i, j]] += 1

    plt.bar(range(256), result, color='black')
    plt.bar(t, np.max(result), color='blue', width=1)
    plt.show()


def optimal_threshold_for(image):

    height, width = image.shape
    minimum, maximum = 256, -1

    for i in range(height):
        for j in range(width):
            minimum = min(minimum, int(image[i, j]))
            maximum = max(maximum, int(image[i, j]))

    t = (minimum + maximum) / 2

    tolerance = 2

    # Calculating optimal threshold
    previous_t = 1000000   # Big value

    while abs(t - previous_t) > tolerance:

        previous_t = t  # Previous t

        mean0 = mean1 = []

        for i in range(0, height):
            for j in range(0, width):
                if image[i, j] > t:
                    mean1.append(image[i, j])
                else:
                    mean0.append(image[i, j])

        mean0 = np.mean(np.array(mean0))
        mean1 = np.mean(np.array(mean1))

        t = int((mean0 + mean1) / 2)

    return t


def global_thresholding(filename):

    image = cv2.imread(filename, 0)
    output = cv2.imread(filename, 0)

    height, width = image.shape

    threshold = optimal_threshold_for(image)
    histogram(image, threshold)

    # Actually performing the thresholding
    for i in range(0, height):
            for j in range(0, width):
                if image[i, j] > threshold:
                    output[i, j] = 255
                else:
                    output[i, j] = 0

    # Display image
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save to file
    cv2.imwrite('gt_%s' % filename, output)


def local_thresholding(filename, ms, a, b):

    image = cv2.imread(filename, 0)
    output = cv2.imread(filename, 0)

    height, width = image.shape

    ms = int(ms / 2)

    g = np.mean(image)

    for i in range(height):
        for j in range(width):

            top = max(i - ms, 0)
            bottom = min(i + ms, height - 1)
            left = max(j - ms, 0)
            right = min(j + ms, width - 1)
            mask = image[top:bottom + 1, left:right + 1]

            std = np.std(mask)
            mean = np.average(mask)

            threshold = a*std + b*mean

            if image[i, j] > threshold:
                output[i, j] = 255
            else:
                output[i, j] = 0

    # Display image
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('lt_%d_%d_%d.png' % (ms*2+1, a, b), output)


global_thresholding('reflectance.png')
# local_thresholding('reflectance.png', 3, 30, 0.2)
