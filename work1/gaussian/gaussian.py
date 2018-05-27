import cv2
import numpy as np


def gaussian_kernel(window, sigma):

    kernel = np.array([np.zeros(window) for _ in range(window)])
    n = window / 2
    s = 0

    for i in range(window):
        yd = n - i
        for j in range(window):
            xd = n - j
            kernel[i, j] = (1 / (2*np.pi * (sigma**2))) * np.exp(-((xd**2 + yd**2) / (2*(sigma**2))))
            s += kernel[i, j]

    factor = 1 / s

    # Correcting the values
    for i in range(window):
        for j in range(window):
            kernel[i, j] *= factor

    return kernel


def gaussian(filename, window, sigma):

    kernel = gaussian_kernel(window, sigma)

    n = window / 2

    image = cv2.imread(filename, 0)       # Input file
    output = cv2.imread(filename, 0)      # Output file

    height, width = image.shape

    for i in range(height):

        for j in range(width):

            s = 0  # Sum
            kr = 0  # Kernel Row

            for k in range(i - n, i + n + 1):
                kc = 0  # Kernel Column
                for l in range(j - n, j + n + 1):
                    if 0 <= k < height and 0 <= l < width:
                        s += image[k, l] * kernel[kr][kc]
                    kc += 1
                kr += 1

            output[i, j] = s

    # Displays the output
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save to file
    cv2.imwrite('gaussian_output_window_%d_sigma_%d.png' % (window, sigma), output)

print 'Calculating...'
gaussian('lena.png', 3, 32)
print 'Done!'

exit(1)
