import unittest
import os
import sys
sys.path.append('/home/alistair/git/D3GET/bin')
import NameWriter

print "1"

class NameWriterTest(unittest.TestCase):
    print "2"
    
    def testNameWrite_write_bad_test(self):
        self.assertEquals(NameWriter.write(12,12), "Bad Arguments")
        
#def main():
    #unittest.main()
    
#if __name__ == '__main__':
    #main()