import os
from numpy import array, concatenate
from IOSift.FeatureReader import FeatureReader

__author__ = 'Agnieszka'


class FeaturePreprocessor():
    def __init__(self, path):
        self.path = path
        self.list_with_features_object = {}
        self.list_with_features_object['prostate'] = []
        self.list_with_features_object['bladder'] = []
        self.list_with_features_object['rectum'] = []
        self.list_with_features_object['femurR'] = []
        self.list_with_features_object['femurL'] = []
        self.list_with_features_object['semi_vesicle'] = []

    def apply(self):

        path = '/CT_analysesClassification/'

        for i in range(1, 4):

            try:
                path = self.path+'/'+ str(i) + '_nd//CT_analysesClassification/'
                if not os.path.exists(path):
                    raise IOError
            except IOError:
                continue
            for o in range(1, 4):
                path_temp = path + str(o) + '/FullFeature/'
                print(path_temp)
                feature_list = FeatureReader(path_temp).open()
                for feature in feature_list:

                    if feature.prostate_keypoints.size != 0:
                        for e in feature.prostate_keypoints:
                            self.list_with_features_object['prostate'].append(e)
                    if feature.bladder_keypoints.size != 0:
                        for e in feature.bladder_keypoints:
                            self.list_with_features_object['bladder'].append(e)
                    if feature.rectum_keypoints.size != 0:
                        for e in feature.rectum_keypoints:
                            self.list_with_features_object['rectum'].append(e)
                    if feature.femurR_keypoints.size != 0:
                        for e in feature.femurR_keypoints:
                             self.list_with_features_object['femurR'].append(e)
                    if feature.femurL_keypoints.size != 0:
                        for e in feature.femurL_keypoints:
                            self.list_with_features_object['femurL'].append(e)
                    if feature.semi_vesicle_keypoints.size != 0:
                        for e in feature.semi_vesicle_keypoints:
                            self.list_with_features_object['semi_vesicle'].append(e)


    def get_feature(self):
        dic_temp = {}

        dic_temp['prostate'] = array(self.list_with_features_object['prostate'])
        print(dic_temp['prostate'].shape)
        dic_temp['bladder'] = array(self.list_with_features_object['bladder'])
        dic_temp['bladder'] = array(self.list_with_features_object['femurL'])
        dic_temp['femurR'] = array(self.list_with_features_object['femurR'])
        dic_temp['femurL'] = array(self.list_with_features_object['femurL'])
        dic_temp['semi_vesicle'] = array(self.list_with_features_object['semi_vesicle'])
        return dic_temp
