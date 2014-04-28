'''
Created on Apr 11, 2014

@author: u0490822
'''

import model

class TilePyramid(model.DirectoryResource):
    '''
    classdocs
    '''
    @property
    def Levels(self):
        return self._levels

    @Levels.setter
    def Levels(self, val):
        self._levels = val

    def AddLevel(self, val):
        assert(isinstance(val, model.Level))
        assert(val not in self._levels)
        self._levels[val.Downsample] = val

    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._levels = {}

        super().__init__(**kwargs)