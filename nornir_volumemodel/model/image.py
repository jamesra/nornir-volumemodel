'''
Created on Apr 11, 2014

@author: u0490822
'''

from . import FileResource

class Image(FileResource):
    '''
    An image file on disk
    '''
    
    @property
    def MaskPath(self):
        return self._maskpath

    def __init__(self, **kwargs):
        '''
        Constructor
        '''
        
        self._maskpath = kwargs.get('MaskPath',None)

        super().__init__(**kwargs)