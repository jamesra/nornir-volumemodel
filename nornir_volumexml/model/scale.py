'''
Created on Apr 11, 2014

@author: u0490822
'''

import model


class Scale(model.ModelBase):
    '''
    classdocs
    '''
    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, val):
        assert(isinstance(val, float))
        self._X = val

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, val):
        assert(isinstance(val, float))
        self._Y = val

    @property
    def Z(self):
        return self._Z

    @Z.setter
    def Z(self, val):
        assert(isinstance(val, float))
        self._Z = val

    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._X = None
        self._Y = None
        self._Z = None

        super().__init__(**kwargs)