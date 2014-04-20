'''
Created on Apr 11, 2014

@author: u0490822
'''
import unittest
import test.test_base
import os

import nornir_volumexml
import nornir_volumexml.model as nmodel



class Test(test.test_base.PlatformTest):

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