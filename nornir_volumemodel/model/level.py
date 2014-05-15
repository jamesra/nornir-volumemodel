'''
Created on Apr 11, 2014

@author: u0490822
'''


from . import DirectoryResource

class Level(DirectoryResource):
    '''
    classdocs
    '''
    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, val):
        self._Number = val

    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._Number = kwargs.pop('Number', None)

        super().__init__(**kwargs)