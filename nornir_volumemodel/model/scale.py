'''
Created on Apr 11, 2014

@author: u0490822
'''


from . import ModelBase


class AxisScale():

    @property
    def UnitsOfMeasure(self):
        return self._UnitsOfMeasure

    @property
    def UnitsPerPixel(self):
        return float(self._UnitsPerPixel)

    def __init__(self, UnitsPerPixel, UnitsOfMeasure):
        self._UnitsOfMeasure = UnitsOfMeasure
        self._UnitsPerPixel = UnitsPerPixel


class Scale(ModelBase):
    '''
    classdocs
    '''
    @property
    def X(self):
        return self._axes['X']

    @X.setter
    def X(self, val):
        assert(isinstance(val, float))
        self._axes['X'] = val

    @property
    def Y(self):
        return self._axes['Y']

    @Y.setter
    def Y(self, val):
        assert(isinstance(val, float))
        self._axes['Y'] = val

    @property
    def Z(self):
        if 'Z' in self._axes:
            return self._axes['Z']

        return None

    @Z.setter
    def Z(self, val):
        assert(isinstance(val, float))
        self._axes['Z'] = val

    @property
    def AxisNames(self):
        return list(self._axes.keys())

    def GetAxis(self, axisname):
        return self._axes.get(axisname, None)

    def SetAxis(self, axisname, UnitsPerPixel, UnitsOfMeasure):
        axis_scale = AxisScale(UnitsPerPixel, UnitsOfMeasure)
        self._axes[axisname] = axis_scale

    def __init__(self, **kwargs):
        '''
        Constructor
        '''
        self._axes = {}
        super().__init__(**kwargs)