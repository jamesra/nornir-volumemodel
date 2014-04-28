'''
Created on Apr 11, 2014

@author: u0490822
'''

import model

class Channel(model.DirectoryResource, model.Named):
    '''
    classdocs
    '''

    @property
    def Filters(self):
        return self._filters

    @Filters.setter
    def Filters(self, val):
        self._filters = val

    def AddFilter(self, val):
        assert(isinstance(val, model.Filter))
        assert(val not in self._filters)
        self._filters[val.Name] = val
        # self._filters.append(val)

    @property
    def Transforms(self):
        return self._transforms

    @Transforms.setter
    def Transforms(self, val):
        self._transforms = val.values()

    def AddTransform(self, val):
        assert(isinstance(val, model.Transform))
        assert(val not in self._transforms)
        self._transforms[val.Name] = val

    @property
    def Scale(self):
        return self._scale

    @Scale.setter
    def Scale(self, val):
        self._scale = val

    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._filters = {}
        self._transforms = {}
        self._scale = None

        super().__init__(**kwargs)
