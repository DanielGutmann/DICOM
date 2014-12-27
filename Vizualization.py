from matplotlib.pyplot import imshow, show
from mayavi import mlab
from mayavi.tools.helper_functions import points3d
from numpy import concatenate
from Normalization import keypoints_concatenate

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
    s=image3D.Image3D
    src = mlab.pipeline.scalar_field(image3D.Image3D)
    src.spacing = image3D.spacing
    src.update_image_data = True
    '''
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
    mlab.pipeline.image_plane_widget(src,
                                     plane_orientation='y_axes',
                                     slice_index=128,
                                     colormap='black-white'

    )
    '''
    mlab.pipeline.iso_surface(src, contours=[s.min()+0.1*s.ptp(), ], opacity=0.5)
    mlab.pipeline.iso_surface(src, contours=[s.max()-0.1*s.ptp(), ],)

    mlab.outline()

    mlab.show()


def keypoints_vizualization(Image3D):
    print(Image3D.keypoints_max.shape[0], Image3D.keypoints_min.shape[0])
    index = keypoints_concatenate(Image3D)
    points3d(index[:, 0], index[:, 1], index[:, 2], mode='point')
    mlab.show()

def keypointsOrinetation_vizualization(Image3D):
    index = Image3D.keypoints_orientation
    points3d(index[:, 0], index[:, 1], index[:, 2], mode='point')
    #x=sin()*cos()
    mlab.show()
