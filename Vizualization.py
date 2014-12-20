from matplotlib.pyplot import imshow, show
from mayavi import mlab
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
    src = mlab.pipeline.scalar_field(image3D.get_image3D())
    src.spacing = image3D.get_spacing()
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
