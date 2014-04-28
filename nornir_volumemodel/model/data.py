'''
Created on Apr 11, 2014

@author: u0490822
'''

import model

class Data(model.FileResource):
    '''
    Represents a file on disk with hashable amount of data
    '''


    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        super().__init__(**kwargs)
