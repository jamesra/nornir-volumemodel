'''
Created on Apr 11, 2014

@author: u0490822
'''


from . import level, DirectoryResource, pyramidinterface

class ImageSet(DirectoryResource, pyramidinterface.PyramidInterface):
    '''
    classdocs
    '''
    
    def _BuildImageDict(self):
        _image_dict = {}
        for l in self.Levels:
            if not l.Image is None:
                self._image_dict[l.Number] = l.Image
                
        return _image_dict 
        
    def GetImages(self):
        return self._BuildImageDict()        

    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._levels = {}
        self._image_dict = None
        super().__init__(**kwargs)