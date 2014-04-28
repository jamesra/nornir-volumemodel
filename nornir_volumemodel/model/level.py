'''
Created on Apr 11, 2014

@author: u0490822
'''

import model

class Level(model.DirectoryResource):
    '''
    classdocs
    '''
    @property
    def Downsample(self):
        return self._Downsample

    @Downsample.setter
    def Downsample(self, val):
        self._Downsample = val

    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._Downsample = None

        super().__init__(**kwargs)