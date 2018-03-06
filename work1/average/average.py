import cv2
import numpy as np


def average(filename, size):

    kernel = np.array([np.ones(size) for _ in range(size)])

    n = size / 2

    image = cv2.imread(filename, 0)       # Input file
    output = cv2.imread(filename, 0)      # Output file

    width, height = image.shape

    for i in range(height):
        for j in range(width):

            tb = max(i - n, 0)            # Top Bound
            bb = min(i + n, height - 1)   # Bottom Bound
            lb = max(j - n, 0)            # Left Bound
            rb = min(j + n, width - 1)    # Right Bound
            s = 0  # Sum

            for k in range(tb, bb + 1):
                for l in range(lb, rb + 1):
                    s += image[k, l] * kernel[k - tb][l - lb]

            output[i, j] = s / (size ** 2)

    # Displays the output
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save to file
    cv2.imwrite('average_output_size_%d.png' % size, output)

print 'Calculating...'
average('lena.png', 9)
print 'Done!'

exit(1)
