from moore import moore_boundary
from chain_code import chain_code
from pre_processing import read_numbers


def max_diameter(image, d):
    n = image.shape[0]
    max_dia = 0
    max_i = -1
    for i in range(n):
        dia = diameter(image, i, d)
        if dia is not None and dia > max_dia:
            max_dia = dia
            max_i = i
    return max_dia, max_i


def max_diameter_horizontal(image):
    return max_diameter(image, 0)


def max_diameter_vertical(image):
    return max_diameter(image, 1)


def diameter(image, i, d):
    n = image.shape[0]

    def pixel(pi, pj, pd):
        if pd == 0:
            return image[pi, pj]
        return image[pj, pi]

    j = 0
    while j < n and pixel(i, j, d) == 0:
        j += 1
    if j >= n:
        return None
    first = j

    j = image.shape[0] - 1
    while j >= 0 and pixel(i, j, d) == 0:
        j -= 1
    if j < 0:
        return None
    last = j

    return last - first + 1


def eccentricity(image):
    hor = max_diameter_horizontal(image)[0]
    ver = max_diameter_vertical(image)[0]
    return float(hor) / float(ver)


def boundary_length(path):
    return len(path)


def compact_chain(chain):
    if len(chain) == 0:
        return ''
    compacted = chain[0]
    for i in range(1, len(chain)):
        if chain[i - 1] != chain[i]:
            compacted += chain[i]
    return compacted


def count_directions(chain, dirs):
    count = 0
    for c in chain:
        if c in dirs:
            count += 1
    return count


def slopes(chain):
    compacted = compact_chain(chain)
    return count_directions(compacted, '1357')


def direction_sum(chain):
    compacted = compact_chain(chain)
    s = 0
    for c in compacted:
        s += int(c)
    return s

class DataPoint:

    def __init__(self, number):
        self.image = number.image
        self.y = number.number
        self.width = -1
        self.height = -1
        self.eccentricity = -1
        self.moore_length = -1
        self.slopes = -1
        self.direction_sum = -1

    def fit(self):
        moore, path = moore_boundary(self.image)
        self.width = max_diameter_horizontal(moore)[0]
        self.height = max_diameter_vertical(moore)[0]
        self.eccentricity = eccentricity(moore)
        self.moore_length = boundary_length(path)

        chain = chain_code(self.image, 4)
        self.slopes = slopes(chain)
        self.direction_sum = direction_sum(chain)

    def __str__(self):
        s = '----- %d -----\n' % self.y
        s += 'Width: %d\n' % self.width
        # s += 'Height: %d\n' % self.height
        # s += 'Eccentricity: %f\n' % self.eccentricity
        s += 'Moore Length: %d\n' % self.moore_length
        s += 'Slopes: %d\n' % self.slopes
        s += 'Direction Sum: %d\n' % self.direction_sum
        return s

    def csv_line(self):
        return '%d,%d,%d,%d,%d' %\
               (self.width, self.moore_length,
                self.slopes, self.direction_sum, self.y)

    @staticmethod
    def csv_header():
        return '%s,%s,%s,%s,%s' %\
               ('Width', 'Moore Length', 'Slopes',
                'DirectionSum', 'Y')


def write_csv(filename, data_points):
    with open(filename, 'wb') as f:
        if len(data_points) > 0:
            f.write(data_points[0].csv_header())
            f.write('\n')
        for p in data_points:
            f.write(p.csv_line())
            f.write('\n')


def generate_dataset():
    numbers = read_numbers(-1, 35)
    data_points = [DataPoint(n) for n in numbers]
    for point in data_points:
        point.fit()
    write_csv('dataset.csv', data_points)


print 'Generating dataset...'
generate_dataset()
print 'Done!'
