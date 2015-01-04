import os
from numpy import array, concatenate, hstack, ones
from IOSift.FeatureReader import FeatureReader

__author__ = 'Agnieszka'


class FeaturePreprocessorPatient():
    def __init__(self, path):
        self.path = path
        self.list_with_features_object = {}
        self.list_with_features_object['prostate'] = []
        self.list_with_features_object['bladder'] = []
        self.list_with_features_object['rectum'] = []
        self.list_with_features_object['femurR'] = []
        self.list_with_features_object['femurL'] = []
        self.list_with_features_object['semi_vesicle'] = []
        self.organs_names = ['rectum', 'prostate', 'bladder', 'femurL', 'femurR', 'semi_vesicle']

    def apply(self):

        path = '/CT_analysesClassification/'

        for i in range(1, 43):

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
                    for orgnas in self.organs_names:
                        if eval('feature.'+orgnas+'_keypoints.size') != 0:
                            for e in eval('feature.'+orgnas+'_keypoints'):

                                self.list_with_features_object[orgnas].append(concatenate((e[3:],[i])))



    def get_feature(self):
        dic_temp = {}
        for orgnas in self.organs_names:
            dic_temp[orgnas] = array(self.list_with_features_object[orgnas])

        return dic_temp

    def get_data_for_classificator(self):
        data=self.get_feature()

        label={}
        i=0
        for orgnas in self.organs_names:
            i+=1
            data[orgnas]=concatenate((data[orgnas],ones((data[orgnas].shape[0],1))*i),axis=1)
            label[i]=orgnas
            if i==1:
                data_temp=data[orgnas]
            else:
                data_temp=concatenate((data_temp,data[orgnas]),axis=0)

        return data_temp,label