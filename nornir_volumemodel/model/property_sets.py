class InputTransformPropertySet(object):

    @property
    def InputTransformChecksum(self):
        return self._InputTransformChecksum

    @InputTransformChecksum.setter
    def InputTransformChecksum(self, value):
        self._InputTransformChecksum = value

    @property
    def InputTransformType(self):
        return self._InputTransformType

    @InputTransformType.setter
    def InputTransformType(self, value):
        self._InputTransformType = value

    def __init__(self, **kwargs):
        self._InputTransformChecksum = None
        self._InputTransformType = None