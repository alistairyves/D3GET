import unittest

import NameWriter

class NameWriterTest(unittest.TestCase):
    
    def setup(self):
        print "its set up"
    
    def NameWrite_write_bad_test(self):
        assertEquals(NameWriter(12,12), "BadArguments")