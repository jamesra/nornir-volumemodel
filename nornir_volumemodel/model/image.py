'''
Created on Apr 11, 2014

@author: u0490822
'''

from . import FileResource

class Image(FileResource):
    '''
    A file on disk
    '''

    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        super().__init__(**kwargs)