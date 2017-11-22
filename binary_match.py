import unittest
import re

PATTERN = re.compile(r'^(1(01*0)*1|0)+$')
       
print(bool(PATTERN.match("11111111111")))


class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(bool(PATTERN.match(" 0")), False)
    
    def test2(self):
        self.assertEqual(bool(PATTERN.match("abc")), False)
    
    def test3(self):
        self.assertEqual(bool(PATTERN.match("000")), True)
    
    def test4(self):
        self.assertEqual(bool(PATTERN.match("110")), True)
    
    def test5(self):
        self.assertEqual(bool(PATTERN.match("111")), False)
    
    def test6(self):
        self.assertEqual(bool(PATTERN.match("{:b}".format(12345678))), True)

if __name__ == '__main__':
    unittest.main()