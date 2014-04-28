'''
Created on Apr 11, 2014

@author: u0490822
'''

import model

class Volume(model.DirectoryResource, model.Named):

    '''
    classdocs
    '''

    @property
    def Blocks(self):
        return self._blocks

    def AddBlock(self, val):
        assert(isinstance(val, model.Block))
        assert(val not in self._blocks)
        self._blocks.append(val)


    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._blocks = []
        self._Parent = None

        super().__init__(**kwargs)
