from pointsPixelFeature import pointsPixelFeature

__author__ = 'Agnieszka'

import unittest


class pointPixelFeatureTest(unittest.TestCase):
    def test_something(self):
        self.path = 'D:/dane/'
        self.feature_preprocessor = pointsPixelFeature(self.path)
        self.feature_preprocessor.apply()


if __name__ == '__main__':
    unittest.main()
