"""
Created on Apr 27, 2016

@author: u0490822
"""


class stos_map:
    """
    Map of slice-to-slice transformations
    """
    _name: str
    _center_section: int
    _mappedToControl: dict[int, set[int]]

    @property
    def CenterSection(self) -> int:
        """
        Section that every other section eventually maps onto
        """
        return self._center_section

    @CenterSection.setter
    def CenterSection(self, val: int | str):
        self._center_section = int(val)

    def AddMapping(self, ControlSection: int, MappedSection: int):
        if MappedSection not in self._mappedToControl:
            self._mappedToControl[MappedSection] = {ControlSection}
        else:
            self._mappedToControl[MappedSection].add(ControlSection)

    def __init__(self, Name: str, CenterSection: int):
        """
        Constructor
        """
        self._name = Name
        self._center_section = CenterSection
        self._mappedToControl = {}


class stos_mapping(object):
    _control: int
    _mapped: int

    @property
    def Control(self) -> int:
        return self._control

    @property
    def Mapped(self) -> int:
        return self._mapped

    def __init__(self, ControlSection: int | str, MappedSection: int | str):
        self._control = int(ControlSection)
        self._mapped = int(MappedSection)
