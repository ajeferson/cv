import cv2
import numpy as np


def sobel(filename):

    image = cv2.imread(filename, 0)
    output = cv2.imread(filename, 0)

    height, width = image.shape

    for i in range(1, height - 1):
        for j in range(1, width - 1):

            # Vertical
            gx = image[i-1, j-1] + 2*image[i, j-1] + image[i+1, j-1] \
                 - image[i-1, j+1] - 2*image[i, j+1] - image[i+1, j+1]
            gy = image[i-1, j-1] + 2*image[i-1, j] + image[i-1, j+1] \
                - image[i+1, j-1] - 2*image[i+1, j] - image[i+1, j+1]
            s = np.sqrt(gx**2 + gy**2)

            # Upper and lower bounds
            s = min(s, 255)
            s = max(s, 0)

            output[i, j] = s

    # Display image
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save to file
    cv2.imwrite('sobel_%s' % filename, output)


sobel('bridge.jpg')
