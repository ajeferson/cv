import cv2
import numpy as np


def median(filename, window):

    n = window / 2

    image = cv2.imread(filename, 0)       # Input file
    output = cv2.imread(filename, 0)      # Output file
    # image = np.array(
    #     [
    #         [1, 2, 3],
    #         [1, 2, 3],
    #         [1, 2, 3]
    #     ]
    # )
    #
    # output = np.array(
    #     [
    #         [1, 2, 3],
    #         [1, 2, 3],
    #         [1, 2, 3]
    #     ]
    # )

    width, height = image.shape

    for i in range(height):
        for j in range(width):

            # Emptying the counting array
            counting = [0 for _ in range(256)]

            tb = max(i - n, 0)            # Top Bound
            bb = min(i + n, height - 1)   # Bottom Bound
            lb = max(j - n, 0)            # Left Bound
            rb = min(j + n, width - 1)    # Right Bound

            for k in range(tb, bb + 1):
                for l in range(lb, rb + 1):
                    index = image[k, l]
                    counting[index] += 1

            # Sorting
            s = []
            for k in range(255):
                while counting[k] > 0:
                    s.append(k)
                    counting[k] -= 1

            if len(s) % 2 != 0:           # Is odd
                output[i, j] = s[len(s)/2]
            else:
                output[i, j] = float((s[len(s)/2] + s[len(s)/2 - 1])) / 2.0   # Even

    # Displays the output
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save to file
    cv2.imwrite('median_output_size_%d.png' % window, output)
    # print output

print 'Calculating...'
median('lena.png', 9)
print 'Done!'

exit(1)
