'''
Created on Apr 11, 2014

@author: u0490822
'''

import os
from xml.etree import ElementTree
import nornir_shared.prettyoutput as prettyoutput

import nornir_volumemodel.persistance.nornir_xml.model_xml_adapters

import nornir_volumemodel.model.section


def __AddVolumeDataFilenameIfNeeded(fullpath):
    [base, ext] = os.path.splitext(fullpath)
    if len(ext) == 0:
        return os.path.join(fullpath, "VolumeData.xml")

    return fullpath


def LoadModelObjectFromXmlPath(fullpath):

    Filename = __AddVolumeDataFilenameIfNeeded(fullpath)
    if not os.path.exists(Filename):
        raise ValueError("Provided volume description file does not exist: " + Filename)

    root_elem = LoadXmlElementFromPath(Filename)
    rootObj = ModelFromXMLElement(root_elem, os.path.dirname(Filename))
    return rootObj


def LoadXmlElementFromPath(fullpath):
    '''Returns root xml element from xml file at fullpath'''
    Filename = __AddVolumeDataFilenameIfNeeded(fullpath)
    if not os.path.exists(Filename):
        raise ValueError("Provided volume description file does not exist: " + Filename)

    return ElementTree.parse(Filename).getroot()


def Load(VolumePath, Create=False, UseCache=True):
    '''Load the volume information for the specified directory or create one if it doesn't exist'''
    rootObj = LoadModelObjectFromXmlPath(VolumePath)
    rootObj.Path = os.path.dirname(VolumePath)

    return rootObj


def Save(XMLPath):
    pass


def GetModelLoadFuncFromTag(tag):

    ExpectedFunction = tag + "Load"
    if ExpectedFunction in nornir_volumemodel.persistance.nornir_xml.model_xml_adapters.__dict__:
        return getattr(nornir_volumemodel.persistance.nornir_xml.model_xml_adapters, ExpectedFunction)

    return nornir_volumemodel.persistance.nornir_xml.model_xml_adapters.DefaultElementLoader


def ModelFromXMLElement(Element, ElementPath):

    load_function = GetModelLoadFuncFromTag(Element.tag)

    if load_function is None:
        return None

    linked_child_obj_list = list(ChildElementObjects(Element, ElementPath))

    try:
        obj = load_function(Element, linked_child_obj_list)
    except nornir_volumemodel.persistance.nornir_xml.model_xml_adapters.UnknownModelException as e:
        # print(str(e))
        return None

    if obj is None:
        raise Exception(str(load_function) + " returned None, it should return an object or an exception.")

    for linked_child in linked_child_obj_list:
        linked_child.Parent = obj

    return obj


def _IsLinkedElement(elem):
    return elem.tag.endswith('_Link')

def _LoadLinkedElement(elem, parent_full_path):
    SubContainerPath = os.path.join(parent_full_path, elem.attrib["Path"])

    try:
        childelem = LoadXmlElementFromPath(SubContainerPath)
    except ValueError as e:
        print("XML meta data was missing, skipped: " + SubContainerPath)
        return None

    return ModelFromXMLElement(childelem, SubContainerPath)

def ChildElementObjects(elem, parent_full_path):
    for child in elem:
        childObj = None

        if _IsLinkedElement(child):
            childObj = _LoadLinkedElement(child, parent_full_path)
        else:
            childObj = ModelFromXMLElement(child, parent_full_path)

        if childObj is None:
            # print("Unable to load object for: " + str(ElementTree.tostring(elem)))
            continue

        if isinstance(childObj, nornir_volumemodel.model.section.Section):
            print("Loaded section %d" % childObj.Number)

        yield childObj