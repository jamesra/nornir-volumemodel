'''
Created on Apr 11, 2014

@author: u0490822
'''

from . import DirectoryResource, Named
from . import block

class Volume(DirectoryResource, Named):

    '''
    classdocs
    '''

    @property
    def Blocks(self):
        return self._blocks

    def AddBlock(self, val):
        assert(isinstance(val, block.Block))
        assert(val not in self._blocks)
        self._blocks.append(val)


    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._blocks = []
        self._Parent = None

        super().__init__(**kwargs)
