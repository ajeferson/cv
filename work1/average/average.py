import cv2


def average(filename, size):

    n = size / 2

    image = cv2.imread(filename, 0)       # Input file
    output = cv2.imread(filename, 0)      # Output file

    height, width = image.shape

    for i in range(height):
        for j in range(width):
            s = 0  # Sum
            for k in range(i - n, i + n + 1):
                for l in range(j - n, j + n + 1):
                    if 0 <= k < height and 0 <= l < width:
                        s += image[k, l]

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
