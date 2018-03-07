import cv2


def multi_thresholding(filename, x, y):

    image = cv2.imread(filename, 0)
    output = cv2.imread(filename, 0)

    height, width = image.shape
    for i in range(0, height):
        for j in range(0, width):
            if image[i, j] > y:
                output[i, j] = 255
            elif image[i, j] > x:
                output[i, j] = 127
            else:
                output[i, j] = 0

    # Display image
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save to file
    cv2.imwrite('multi_thresholding_%d_%d_%s' % (x, y, filename), output)

multi_thresholding('chaplin.jpg', 160, 220)


