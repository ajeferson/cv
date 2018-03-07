import cv2


def median(filename, window):

    n = window / 2

    image = cv2.imread(filename, 0)       # Input file
    output = cv2.imread(filename, 0)      # Output file

    height, width = image.shape

    for i in range(height):

        for j in range(width):

            s = 0  # Sum
            kr = 0  # Kernel Row

            # Emptying the counting array
            counting = [0 for _ in range(256)]

            # Counting values
            for k in range(i - n, i + n + 1):
                kc = 0  # Kernel Column
                for l in range(j - n, j + n + 1):
                    if 0 <= k < height and 0 <= l < width:
                        index = image[k, l]
                        counting[index] += 1
                    kc += 1
                kr += 1

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

print 'Calculating...'
median('lena.png', 9)
print 'Done!'

exit(1)
