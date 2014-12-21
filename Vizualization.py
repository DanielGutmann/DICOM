from matplotlib.pyplot import imshow, show
from mayavi import mlab
from mayavi.tools.helper_functions import points3d
from numpy import concatenate

__author__ = 'Agnieszka'


def visualization2D(image2D):
    """

    :param image2D: array with 2D image
    :return:void
    """
    imshow(image2D, cmap='gray')
    show()


def visualization3D(image3D):
    """
    :param image3D: image object from readDirWithBinaryDAta
    :return:
    """
    src = mlab.pipeline.scalar_field(image3D.Image3D)
    src.spacing = image3D.spacing
    src.update_image_data = True
    mlab.pipeline.image_plane_widget(src,
                                     plane_orientation='x_axes',
                                     slice_index=128,
                                     colormap='black-white'
    )
    mlab.pipeline.image_plane_widget(src,
                                     plane_orientation='z_axes',
                                     slice_index=35,
                                     colormap='black-white'

    )
    mlab.outline()

    mlab.show()


def keypoints_vizualization(Image3D):
    print(Image3D.keypoints_max.shape[0], Image3D.keypoints_min.shape[0])
    if Image3D.keypoints_max.shape[0] == 0 and Image3D.keypoints_min.shape[0]==0:
        return
    elif Image3D.keypoints_max.shape[0] == 0:
        index = Image3D.keypoints_min

    elif Image3D.keypoints_min.shape[0] == 0:
        index = Image3D.keypoints_max


    else:
        index = concatenate((Image3D.keypoints_max, Image3D.keypoints_min))
    points3d(index[:, 0], index[:, 1], index[:, 2], mode='point')
    mlab.show()

