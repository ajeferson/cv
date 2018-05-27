from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import numpy as np
import cv2


def do_watershed(filename):

    # load the image and perform pyramid mean shift filtering to aid the thresholding step
    image = cv2.imread(filename)
    output = cv2.imread(filename)
    shifted = cv2.pyrMeanShiftFiltering(image, 21, 51)

    gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255,
                           cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    D = ndimage.distance_transform_edt(thresh)
    localMax = peak_local_max(D, indices=False, min_distance=20, labels=thresh)

    # perform a connected component analysis on the local peaks, using 8-connectivity, then appy the Watershed algorithm
    markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
    labels = watershed(-D, markers, mask=thresh)

    for label in np.unique(labels):

        # Do nothing with background
        if label == 0:
            continue

        # otherwise, allocate memory for the label region and draw it on the mask
        mask = np.zeros(gray.shape, dtype='uint8')
        mask[labels == label] = 255

        # detect contours in the mask and grab the largest one
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        c = max(cnts, key=cv2.contourArea)

        # Drawing circle
        ((x, y), r) = cv2.minEnclosingCircle(c)
        cv2.circle(output, (int(x), int(y)), int(r), (0, 255, 0), 2)

    cv2.imshow("output", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

do_watershed('coins.jpg')
