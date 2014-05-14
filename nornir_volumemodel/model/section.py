'''
Created on Apr 11, 2014

@author: u0490822
'''

from . import DirectoryResource, Numbered
from . import channel

class Section(DirectoryResource, Numbered):
    '''
    classdocs
    '''
    @property
    def Channels(self):
        return self._channels

    @Channels.setter
    def Channels(self, val):
        self._channels = val

    def AddChannel(self, val):
        assert(isinstance(val, channel.Channel))
        assert(val not in self._channels)
        self._channels.append(val)

    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._channels = []

        super().__init__(**kwargs)