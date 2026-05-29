'''
Created on Apr 11, 2014

@author: u0490822
'''
import importlib.util
import os
import unittest
from pathlib import Path

import nornir_volumexml
import nornir_volumexml.model as nmodel

_spec = importlib.util.spec_from_file_location(
    "nornir_volumemodel_test_base",
    Path(__file__).resolve().parent / "test_base.py",
)
assert _spec is not None and _spec.loader is not None
_test_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_test_base)
PlatformTest = _test_base.PlatformTest


class Test(PlatformTest):

    @property
    def VolumePath(self):
        return "RC2_4Square_Aligned"

    @property
    def Platform(self):
        return "IDOC"

    def test_Load(self):

        VolumeXML = os.path.join(self.ImportedDataPath, 'VolumeData.xml')

        volume = nornir_volumexml.Load_Xml(VolumeXML)
        self.assertIsNotNone(volume)
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()