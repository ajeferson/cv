import cv2
from Queue import Queue

seeds = []


def on_mouse(*args):

    if len(args) < 3:
        return

    event, x, y = args[0], args[1], args[2]
    if event == cv2.EVENT_LBUTTONUP:
        seeds.append((y, x))


def image_growing(filename):

    image = cv2.imread(filename, 0)
    output = cv2.imread(filename, 0)

    # Defining seeds
    cv2.namedWindow('input')
    cv2.setMouseCallback('input', on_mouse, 0)
    cv2.imshow('input', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    for seed in seeds:
        grow_seed(image, output, seed, 5)

    # Display image
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def grow_seed(image, output, seed, threshold):

    height, width = image.shape

    visited = {}

    queue = Queue()

    queue.put(seed)

    gray = int(image[seed])
    output[seed] = 0

    while not queue.empty():

        x, y = queue.get()
        visited[(x, y)] = True

        # Top
        if not (x - 1, y) in visited and x > 0 and abs(gray - image[x - 1, y]) < threshold:
            output[x - 1, y] = 0
            queue.put((x - 1, y))
            visited[(x - 1, y)] = True

        # Bottom
        if not (x + 1, y) in visited and x < height and abs(gray - image[x + 1, y]) < threshold:
            output[x + 1, y] = 0
            queue.put((x + 1, y))
            visited[(x + 1, y)] = True

        # Left
        if not (x, y - 1) in visited and y > 0 and abs(gray - image[x, y - 1]) < threshold:
            output[x, y - 1] = 0
            queue.put((x, y - 1))
            visited[(x, y - 1)] = True

        # Right
        if not (x, y + 1) in visited and y < width and abs(gray - image[x, y + 1]) < threshold:
            output[x, y + 1] = 0
            queue.put((x, y + 1))
            visited[(x, y + 1)] = True

        # Top Left
        if not (x - 1, y - 1) in visited and x > 0 and y > 0 and abs(gray - image[x - 1, y - 1]) < threshold:
            output[x - 1, y - 1] = 0
            queue.put((x - 1, y - 1))
            visited[(x - 1, y - 1)] = True

        # Top Right
        if not (x - 1, y + 1) in visited and x > 0 and y < width and abs(gray - image[x - 1, y + 1]) < threshold:
            output[x - 1, y + 1] = 0
            queue.put((x - 1, y + 1))
            visited[(x - 1, y + 1)] = True

        # Bottom Left
        if not (x + 1, y - 1) in visited and x < height and y > 0 and abs(gray - image[x + 1, y - 1]) < threshold:
            output[x + 1, y - 1] = 0
            queue.put((x + 1, y - 1))
            visited[(x + 1, y - 1)] = True

        # Bottom Right
        if not (x + 1, y + 1) in visited and x < height and y < width and abs(gray - image[x + 1, y + 1]) < threshold:
            output[x + 1, y + 1] = 0
            queue.put((x + 1, y + 1))
            visited[(x + 1, y + 1)] = True


image_growing('triangle.jpg')
