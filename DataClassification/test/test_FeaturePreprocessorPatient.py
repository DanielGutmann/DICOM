from DataClassification.FeaturePreprocessor import FeaturePreprocessor
from DataClassification.FeaturePreprocessorPatient import FeaturePreprocessorPatient

__author__ = 'Agnieszka'
import unittest


class FeaturePreprocessorTest(unittest.TestCase):
    def setUp(self):
        self.path = 'D:/dane/'
        self.feature_preprocessor = FeaturePreprocessorPatient(self.path)
        self.feature_preprocessor.apply()


    def test_number_of_organs(self):
        self.assertEqual(len(self.feature_preprocessor.list_with_features_object), 6)



    def test_get_features(self):
        dic = self.feature_preprocessor.get_feature()
        self.organs_names = ['rectum', 'prostate', 'bladder', 'femurL', 'femurR', 'semi_vesicle']
        import numpy as np
        for orgnas in self.organs_names:
                x=np.bincount(dic[orgnas][:,-1].astype(dtype=np.int8))
                x=x[x!=0]
                print(x)
                print(orgnas,x.mean(),x.std())

    def test_get_classificator(self):
        dic = self.feature_preprocessor.get_data_for_classificator()



if __name__ == '__main__':
        unittest.main()
