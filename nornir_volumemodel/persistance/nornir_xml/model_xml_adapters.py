'''
Adapter functions load volume objects based on Nornir's original XML storage format.

All loaders should return an object.  If an object cannot be returned an exception should 
be raised.
'''
import os
from xml.etree import ElementTree

import nornir_volumemodel.model as model
import datetime


defaultAttributeTypeMapping = {'Downsample' : float,
                               'ImageFormatExt' : str,
                               'InputTransformChecksum' : bytes.fromhex,
                               'InputTransformType': str,
                               'LevelFormat' : str,
                               'Name' : str,
                               'Number' : int,
                               'NumberOfTiles' : int,
                               'Overlap' : float,
                               'Path' : str,
                               'Type' : str,
                               'CreationDate' : str,
                               }

hexChecksumAttributeTypeMapping = {'Checksum' : bytes.fromhex}

filesizeChecksumAttributeTypeMapping = {'Checksum' : int}


def LoadElement(path):
    return ElementTree.parse(path).getroot()

def AddKnownAttributes(elem, obj, mapping):

    for attribname in mapping.keys():
        if attribname in elem.attrib:
            # print(attribname + " = " + str(elem.attrib[attribname]))
            val = mapping[attribname](elem.attrib[attribname])

            setattr(obj, attribname, val)
            # Make sure our setters are working
            assert(getattr(obj, attribname) == val)


def TryGetModelClass(name):

    if name in model.__dict__:
        return getattr(model, name)

    return None


def DefaultElementLoader(elem, childObjs):
    '''The default loader for an element'''
    classObj = TryGetModelClass(elem.tag)
    if classObj is None:
        raise Exception("Unknown model type: " + elem.tag)

    obj = classObj()
    AddKnownAttributes(elem, obj, defaultAttributeTypeMapping)

    return obj

def VolumeLoad(elem, childObjs):

    obj = model.Volume()

    AddKnownAttributes(elem, obj, defaultAttributeTypeMapping)

    for child in childObjs:
        if isinstance(child, model.Block):
            obj.AddBlock(child)

    return obj

def BlockLoad(elem, childObjs):

    obj = model.Block()

    AddKnownAttributes(elem, obj, defaultAttributeTypeMapping)

    for child in childObjs:
        if isinstance(child, model.Section):
            obj.AddSection(child)

    return obj


def SectionLoad(elem, childObjs):

    obj = model.Section()

    AddKnownAttributes(elem, obj, defaultAttributeTypeMapping)

    for child in childObjs:
        if isinstance(child, model.Channel):
            obj.AddChannel(child)

    return obj


def ChannelLoad(elem, childObjs):

    obj = model.Channel()

    AddKnownAttributes(elem, obj, defaultAttributeTypeMapping)

    for child in childObjs:
        if isinstance(child, model.Filter):
            obj.AddFilter(child)

        if isinstance(child, model.Transform):
            obj.AddTransform(child)

        if isinstance(child, model.Scale):
            obj.Scale = child

    return obj


def FilterLoad(elem, childObjs):

    obj = model.Filter()

    AddKnownAttributes(elem, obj, defaultAttributeTypeMapping)

    for child in childObjs:
        if isinstance(child, model.TilePyramid):
            obj.TilePyramid = child

        if isinstance(child, model.Transform):
            obj.AddTransform(child)

    return obj

def TransformLoad(elem, childObjs):

    obj = model.Transform()

    AddKnownAttributes(elem, obj, defaultAttributeTypeMapping)
    AddKnownAttributes(elem, obj, hexChecksumAttributeTypeMapping)

    return obj

def TilePyramidLoad(elem, childObjs):

    obj = model.TilePyramid()

    AddKnownAttributes(elem, obj, defaultAttributeTypeMapping)

    for child in childObjs:
        if isinstance(child, model.Level):
            obj.AddLevel(child)

    return obj

def LevelLoad(elem, childObjs):

    obj = model.Level()

    AddKnownAttributes(elem, obj, defaultAttributeTypeMapping)

    return obj

def ScaleLoad(elem, childObjs):

    scaleAttribMapping = {'X' : float,
                          'Y' : float,
                          'Z' : float}


    obj = model.Scale()

    for child in elem:
        if 'UnitsPerPixel' in child.attrib:
            units_per_pixel = child.attrib['UnitsPerPixel']
            units_of_measure = child.attrib['UnitsOfMeasure']

            obj.SetAxis(child.tag, units_per_pixel, units_of_measure)

    AddKnownAttributes(elem, obj, scaleAttribMapping)

    return obj

if __name__ == '__main__':
    pass