import cv2


def thresholding(filename, x):

    image = cv2.imread(filename, 0)
    output = cv2.imread(filename, 0)

    height, width = image.shape
    for i in range(0, height):
        for j in range(0, width):
            if image[i, j] > x:
                output[i, j] = 255
            else:
                output[i, j] = 0

    # Display image
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save to file
    cv2.imwrite('thresholding_%d_%s' % (x, filename), output)

thresholding('chaplin.jpg', 0)

