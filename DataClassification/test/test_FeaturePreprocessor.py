from DataClassification.FeaturePreprocessor import FeaturePreprocessor

__author__ = 'Agnieszka'
import unittest


class FeaturePreprocessorTest(unittest.TestCase):
    def setUp(self):
        self.path = 'D:/dane/'
        self.feature_preprocessor = FeaturePreprocessor(self.path)
        self.feature_preprocessor.apply()


    def test_number_of_organs(self):
        self.assertEqual(len(self.feature_preprocessor.list_with_features_object), 6)



    def test_get_features(self):
        dic = self.feature_preprocessor.get_feature()

    def test_get_classificator(self):
        dic = self.feature_preprocessor.get_data_for_classificator()



if __name__ == '__main__':
        unittest.main()
