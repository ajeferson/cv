import cv2
import numpy as np


def hough_lines(filename):

    image = cv2.imread(filename)
    output = cv2.imread(filename)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a edge detection filter
    edges = cv2.Canny(gray, 50, 150, apertureSize = 3)

    # Applying Hough Transform
    min_line_length = 100
    max_line_gap = 10
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,min_line_length,max_line_gap)

    # Drawing lines on the output image
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(output, (x1, y1), (x2, y2), (0, 255, 0), 3)

    # Display image
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

hough_lines('window.jpg')
