'''
Created on Apr 11, 2014

@author: u0490822
'''

import os

class ModelBase(object):
    '''Properties common to all volume objects'''

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Value):
        self._Version = Value

    def __init__(self):
        self._Version = None
        self._Parent = None


class ExternalResource(ModelBase):
    '''Properties of objects whose data is stored outside the object file structure, such as on a file system'''

    @property
    def Parent(self):
        return self._Parent

    @Parent.setter
    def Parent(self, Value):
        self._Parent = Value

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, val):
        self._Path = val

        if hasattr(self, '__fullpath'):
            del self.__dict__['__fullpath']

    @property
    def FullPath(self):

        FullPathStr = self.__dict__.get('__fullpath', None)

        if FullPathStr is None:
            FullPathStr = self.Path

            if(not hasattr(self, '_Parent')):
                raise Exception("FullPath could not be generated for resource")

            IterElem = self.Parent

            while not IterElem is None:
                if hasattr(IterElem, 'FullPath'):
                    FullPathStr = os.path.join(IterElem.FullPath, FullPathStr)
                    IterElem = None
                    break
                elif hasattr(IterElem, '_Parent'):
                    IterElem = IterElem._Parent
                else:
                    raise Exception("FullPath could not be generated for resource")

            self.__dict__['__fullpath'] = FullPathStr


        return FullPathStr

    def __init__(self):
        self._Path = None

class DirectoryResource(ExternalResource):
    pass


class Named():
    '''Object that contains other objects.  Path always refers to a directory'''

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, val):
        self._Name = val

    def __init__(self):
        self._Name = None

    def __str__(self):
        return self.Name


class Numbered():
    '''Object that contains other objects.  Path always refers to a directory'''

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, val):
        self._Number = val

    def __init__(self):
        self._Number = None

    def __str__(self):
        return "%d" % self.Number


class FileResource(ExternalResource):
    '''Represents a file'''

    @property
    def Type(self):
        return self._type

    @Type.setter
    def Type(self, value):
        self._type = value

    @property
    def Checksum(self):
        return self._checksum

    @Checksum.setter
    def Checksum(self, val):
        assert(isinstance(val, bytes))
        self._checksum = val

    def __init__(self):
        self._type = None
        self._checksum = None



