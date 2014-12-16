from localExtermum import LocalExterma3D


__author__ = 'Agnieszka'

import unittest


class LocalExtrema3DTest(unittest.TestCase):
    def setUp(self):
        path = './test_data/1_nd/npy_arrays_3DDoG'

        self.local_extrema = LocalExterma3D(path)

    def test_find(self):
        self.image3D_after_log = self.local_extrema.find()


if __name__ == '__main__':
    unittest.main()