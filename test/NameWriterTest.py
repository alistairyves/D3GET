import unittest
import os
import sys
sys.path.append('/home/alistair/git/D3GET/bin/')
import NameWriter


class NameWriterTest(unittest.TestCase):
    
    def testNameWrite_write_notstrings(self):
        self.assertEquals(NameWriter.write(12,12), 'Bad Arguments')
        
    def testNameWrite_write_badnumber(self):
        self.assertEquals(NameWriter.write('blah', '12344'), 'invalid battlenumber length')
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()