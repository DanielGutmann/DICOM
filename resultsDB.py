__author__ = 'Agnieszka'

import anydbm


class ResultsDB(object):
    def __init__(self, data_base_name, path='./'):
        self.path = path
        self.DB = anydbm.open(data_base_name, 'c')

    def open(self, key):
        return self.DB[str(key)]

    def save(self, key, elelment_to_save):
        self.DB[str(key)] = elelment_to_save

    def close(self):
        self.DB.close()