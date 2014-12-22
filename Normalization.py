from numpy import concatenate, array

__author__ = 'Agnieszka'


def normalize(image, range_of_image, new_range):
    a = new_range[0]
    b = new_range[1]
    im = image
    max_o = range_of_image[1]
    min_o = range_of_image[0]
    im = a + ((im - min_o ) * (b - a)) / (max_o - min_o)
    return im

def keypoints_concatenate(Image3D):
    if Image3D.keypoints_max.shape[0] == 0 and Image3D.keypoints_min.shape[0]==0:
        return array([0,0,0])
    elif Image3D.keypoints_max.shape[0] == 0:
        index = Image3D.keypoints_min

    elif Image3D.keypoints_min.shape[0] == 0:
        index = Image3D.keypoints_max

    else:
        index = concatenate((Image3D.keypoints_max, Image3D.keypoints_min))
    return index

