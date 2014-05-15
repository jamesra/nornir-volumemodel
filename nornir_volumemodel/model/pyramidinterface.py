'''
Created on May 14, 2014

@author: u0490822
'''


from operator import attrgetter
from . import level

class PyramidInterface(object):
    '''Presents an interface for image pyramids'''

    @property
    def Levels(self):
        return sorted(self._levels.values(), key=attrgetter('Number'))

    @property
    def MaxResLevel(self):
        '''Return the level with the highest resolution'''
        return self._levels[0]

    @property
    def MinResLevel(self):
        '''Return the level with the highest resolution'''
        return self._levels[-1]

    def GetLevel(self, Number):
        '''
            :param float Number: Level number
            :return: Level node
            :rtype Level:
        '''
        return self._levels[Number]

    def GetOrCreateLevel(self, Number, GenerateData=True):
        '''
            :param float Number: Level Number factor from full-res data
            :param bool Generate: True if missing data should be generated.  Defaults to true.
            :return: Level node for Number node 
            :rtype LevelNode:
        '''
        if not self.HasLevel(Number) and GenerateData:
            self.GenerateLevels(Number)

        levelObj = level.Level(Number=Number)
        self.AddLevel(levelObj)
        levelObj = self.GetLevel(Number)
        assert(not levelObj is None)

    def GenerateLevels(self, Numbers):
        '''Creates data to populate a level of a pyramid.  Derived class should override
        :param list Numbers: Levels to be generated'''
        raise NotImplementedError('PyramidLevelHandler.GenerateMissingLevel')

    def AddLevel(self, val):
        '''Add the passed level object to the pyramid.  Derived class should override'''
        assert(isinstance(val, level.Level))
        assert(val not in self._levels)
        self._levels[val.Number] = val

    def HasLevel(self, Number):
        return not self.GetLevel(Number) is None

    def CreateLevels(self, Levels):
        assert(isinstance(Levels, list))
        for l in Levels:
            self.GetOrCreateLevel(l)

    def LevelIndex(self, Number):
        '''Returns the index number into the level nodes.  Levels with a lower index are more detailed, i.e. less downsampling.  Higher indicies are less detailed.'''
        for i, obj in enumerate(self.Levels):
            if float(Number) == float(obj.Number):
                return i

        raise Exception("Number level does not exist in levels")

    def GetMoreDetailedLevel(self, Number):
        '''Return an existing level with more detail than the provided Number level'''
        BestChoice = None
        LevelList = self.Levels
        LevelList.reverse()

        for Level in LevelList:
            if Level.Number < Number:
                return Level
            else:
                continue

        return BestChoice

    def GetMoreOrEquallyDetailedLevel(self, Number):
        '''Return an existing level with more detail than the provided Number level'''
        BestChoice = None

        LevelList = self.Levels
        LevelList.reverse()
        for Level in LevelList:
            if Level.Number <= Number:
                return Level
            else:
                continue

        return BestChoice

    def GetLessDetailedLevel(self, Number):
        '''Return an existing level with less detail than the provided Number level'''

        for Level in self.Levels:
            if Level.Number > Number:
                return Level