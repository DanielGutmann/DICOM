__author__ = 'Agnieszka'


def normalize(image, range_of_image, new_range):
    a = new_range[0]
    b = new_range[1]
    im = image
    max_o = range_of_image[1]
    min_o = range_of_image[0]
    im = a + ((im - min_o ) * (b - a)) / (max_o - min_o)
    return im

