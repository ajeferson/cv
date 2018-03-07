import cv2
import numpy as np


def laplacian(filename, size, center):

    n = size / 2

    kernel = np.array([np.ones(size) for _ in range(size)])
    kernel[n, n] = center

    image = cv2.imread(filename, 0)       # Input file
    output = cv2.imread(filename, 0)      # Output file
    media = cv2.imread(filename, 0)      # Output file

    height, width = image.shape

    # First, calculate the average
    for i in range(n, height - n):
        for j in range(n, width - n):
            s = 0  # Sum
            kr = 0  # Kernel Row
            for k in range(i - n, i + n + 1):
                kc = 0  # Kernel Column
                for l in range(j - n, j + n + 1):
                    s += image[k, l]
                    kc += 1
                kr += 1

            media[i, j] = s / (size ** 2)

    # Then Laplacian filter
    for i in range(n, height - n):
        for j in range(n, width - n):
            s = 0  # Sum
            kr = 0 # Kernel Row
            for k in range(i - n, i + n + 1):
                kc = 0  # Kernel Column
                for l in range(j - n, j + n + 1):
                    s += media[k, l] * kernel[kr][kc]
                    kc += 1
                kr += 1
            output[i, j] = s + 100

    # for x in range(1, 511):
    #         for y in range(1, 511):
    #             output[x, y] = (media[x, y] * -8 + media[x, y-1] + media[x-1, y] +  media[x+1, y] + media[x, y+1] +
    #                          media[x-1, y-1] + media[x+1, y-1] + media[x-1, y+1] + media[x+1, y+1])
    #             output[x, y] += 100
    #
    # print output

    # Displays the output
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # # Save to file
    cv2.imwrite('laplacian_output_size_%d_center_%d.png' % (size, center), output)

print 'Calculating...'
laplacian('goku.jpg', 5, -8)
print 'Done!'

exit(1)
