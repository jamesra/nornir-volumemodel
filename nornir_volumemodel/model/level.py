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
    
    @property
    def Image(self):
        return self._image
    
    @Image.setter
    def Image(self, value):
        self._image = value

    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._Number = kwargs.pop('Number', None)
        self._image = None

        super().__init__(**kwargs)