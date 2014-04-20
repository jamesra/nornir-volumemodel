'''
Created on Apr 11, 2014

@author: u0490822
'''
import unittest

import nornir_volumexml.model as model

class Test(unittest.TestCase):


    def test_volume(self):

        vol = model.Volume()
        vol.Name = "TestVolume"


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()