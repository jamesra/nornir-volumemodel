'''
Created on Apr 11, 2014

@author: u0490822
'''

from . import DirectoryResource, Named

class Filter(DirectoryResource, Named):
    '''
    classdocs
    '''
    @property
    def TilePyramid(self):
        return self._tilepyramid

    @TilePyramid.setter
    def TilePyramid(self, val):
        self._tilepyramid = val

    @property
    def HistogramData(self):
        return self._histogram

    @HistogramData.setter
    def HistogramData(self, val):
        self._histogram = val

    @property
    def PruneData(self):
        return self._prune

    @PruneData.setter
    def PruneData(self, val):
        self._prune = val

    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._tilepyramid = None
        self._prune = None
        self._histogram = None

        super().__init__(**kwargs)