from OpenMask import OpenMask
from Read_Mask import ReadMask
from Vizualization import visualization3D_notimage

__author__ = 'Agnieszka'

import unittest

class OpenMaskTest(unittest.TestCase):

    def test_init(self):
        OpenMask('./test_data/1_nd/')

    def test_read_mask(self):
        maski=ReadMask('./test_data/1_nd/CT_analyses/').openMask()
        visualization3D_notimage(maski.prostate)
