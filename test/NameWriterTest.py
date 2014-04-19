import unittest
import os

#import bin.NameWriter
#import D3GET.bin.NameWriter
from .bin.NameWriter import NameWriter
print "1"

class NameWriterTest(unittest.TestCase):
    print "2"
    
    def testNameWrite_write_bad_test(self):
        self.assertEquals(NameWriter(12,12), "BadArguments")
        
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()