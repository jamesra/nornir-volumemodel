'''
Created on Apr 27, 2016

@author: u0490822
'''

class stos_map(object):
    '''
    classdocs
    '''
     
    @property
    def CenterSection(self):
        return self._center_section
    
    @CenterSection.setter
    def CenterSection(self, val):
        self._center_section = int(val)
        
    def AddMapping(self, ControlSection, MappedSection):
        if not MappedSection in self._mappedToControl:
            self._mappedToControl[MappedSection] = set([ControlSection])
        else:
            self._mappedToControl[MappedSection].add(ControlSection)

    def __init__(self, Name, CenterSection):
        '''
        Constructor
        '''
        self._name = Name
        self._center_section = CenterSection
        self._mappedToControl = {}
        
        
class stos_mapping(object):
    
    @property
    def Control(self):
        return self._control
    
    @property
    def Mapped(self):
        return self._mapped
    
    def __init__(self, ControlSection, MappedSection):
        self._control = int(ControlSection)
        self._mapped = int(MappedSection)