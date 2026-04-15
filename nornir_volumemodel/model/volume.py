'''
Created on Apr 11, 2014

@author: u0490822
'''

from . import DirectoryResource, Named
from . import block

class Volume(DirectoryResource, Named):
    """Top-level container for a Nornir-registered electron-microscopy volume.

    A ``Volume`` is the root of the object hierarchy.  It owns one or more
    :class:`~nornir_volumemodel.model.block.Block` objects, each of which
    groups a contiguous run of Z-sections and their associated image channels,
    filters, tile pyramids, and registration transforms.

    Typical usage::

        import nornir_volumemodel
        vol = nornir_volumemodel.Load_Xml('/path/to/volume.xml')
        for block in vol.Blocks:
            for section in block.Sections:
                print(section.Number)
    """

    @property
    def Blocks(self):
        """List of :class:`~nornir_volumemodel.model.block.Block` objects in this volume."""
        return self._blocks

    def AddBlock(self, val):
        """Append a block to this volume.

        :param block.Block val: Block to add; must not already be present.
        :raises AssertionError: if ``val`` is not a ``Block`` or is a duplicate.
        """
        assert(isinstance(val, block.Block))
        assert(val not in self._blocks)
        self._blocks.append(val)


    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._blocks = []
        self._Parent = None

        super().__init__(**kwargs)
