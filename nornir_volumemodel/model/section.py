'''
Created on Apr 11, 2014

@author: u0490822
'''

from . import DirectoryResource, Numbered
from . import channel

class Section(DirectoryResource, Numbered):
    """One physical Z-slice (section) of the volume.

    A ``Section`` is identified by its integer ``Number`` (the Z-level in the
    volume stack).  It holds one or more imaging
    :class:`~nornir_volumemodel.model.channel.Channel` objects — e.g. ``TEM``
    and ``Leveled`` — each of which owns filters, tile pyramids, and
    registration transforms.
    """

    @property
    def Channels(self):
        """List of :class:`~nornir_volumemodel.model.channel.Channel` objects for this section."""
        return self._channels

    @Channels.setter
    def Channels(self, val):
        self._channels = val

    def AddChannel(self, val):
        """Append a channel to this section.

        :param channel.Channel val: Channel to add; must not already be present.
        :raises AssertionError: if ``val`` is not a ``Channel`` or is a duplicate.
        """
        assert(isinstance(val, channel.Channel))
        assert(val not in self._channels)
        self._channels.append(val)

    def __init__(self, **kwargs):
        self._channels = []

        super().__init__(**kwargs)