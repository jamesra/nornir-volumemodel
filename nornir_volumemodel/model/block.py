'''
Created on Apr 11, 2014

@author: u0490822
'''

from . import DirectoryResource, Named
from . import section
from . import stos_map

class Block(DirectoryResource, Named):
    """A grouping of contiguous Z-sections within a volume.

    A ``Block`` is the second level of the volume hierarchy (``Volume → Block →
    Section → Channel …``).  In a typical Nornir experiment one block spans all
    physical sections, but the model allows multiple named blocks (e.g. separate
    tissue blocks imaged in the same experiment).

    Blocks own:

    * A list of :class:`~nornir_volumemodel.model.section.Section` objects.
    * Optional section-to-section (STOS) alignment groups and maps.
    """

    @property
    def Sections(self):
        """List of :class:`~nornir_volumemodel.model.section.Section` objects in this block."""
        return self._sections

    def AddSection(self, val):
        """Append a section to this block.

        :param section.Section val: Section to add; must not already be present.
        :raises AssertionError: if ``val`` is not a ``Section`` or is a duplicate.
        """
        assert(isinstance(val, section.Section))
        assert(val not in self._sections)
        self._sections.append(val)

    def StosGroups(self):
        """Return the dictionary of section-to-section alignment groups keyed by group name."""
        return self._stos_groups

    def StosMaps(self):
        """Return the dictionary of STOS alignment maps keyed by map name."""
        return self._stos_maps

    def __init__(self, **kwargs):
        self._sections = []
        self._stos_groups = {}
        self._stos_maps = {}

        super().__init__(**kwargs)