import cv2
import numpy as np


def hough_circles(filename):

    # Load image
    image = cv2.imread(filename)
    output = image.copy()

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect circles in the image
    min_dist = 100
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, min_dist)

    # ensure at least some circles were found
    if circles is not None:

        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # Draw circles
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 0, 255), 4)

        # show the output image
        cv2.imshow("output", output)
        cv2.waitKey(0)

        cv2.imwrite('hough_circles_output.png', output)


hough_circles('ncircles.jpg')

