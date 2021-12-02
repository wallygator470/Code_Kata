import unittest
#import math
#import re

#def zeros(x):
    #return len(re.sub(r"(^0*)", str(math.factorial(x))[::-1]), "", )
def zeros(n):
    zeros = 0
    i = 5
    while n // i > 0:
        zeros += n // i
        i *= 5
    return zeros
    
class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(zeros(6), 1)
    
    def test2(self):
        self.assertEqual(zeros(12), 2)
    
    def test3(self):
        self.assertEqual(zeros(100), 24)
    
if __name__ == '__main__':
    unittest.main()
