'''
Created on Apr 11, 2014

@author: u0490822
'''

from . import DirectoryResource, Named
from . import section

class Block(DirectoryResource, Named):
    '''
    classdocs
    '''
    @property
    def Sections(self):
        return self._sections

    def AddSection(self, val):
        assert(isinstance(val, section.Section))
        assert(val not in self._sections)
        self._sections.append(val)

    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._sections = []

        super().__init__(**kwargs)
