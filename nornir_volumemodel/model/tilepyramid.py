'''
Created on Apr 11, 2014

@author: u0490822
'''

from . import level, DirectoryResource, pyramidinterface

class TilePyramid(DirectoryResource, pyramidinterface.PyramidInterface):
    '''
    classdocs
    '''

    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._levels = {}

        super().__init__(**kwargs)