import unittest
import os
import sys
sys.path.append('/home/alistair/git/D3GET/bin/')
from name_writer import NameWriter
import json
import simplejson


class NameWriterTest(unittest.TestCase):
    
    def setUp(self):
        print "Setting up"
        #nw = NameWriter()
        
    def testNameWrite_write_badnumber(self):
        nw = NameWriter()
        self.assertEquals(nw.write(battlename='blah', battlenumber='12344'), 'invalid battlenumber length')
    
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()