#import unittest

MULTIPLIER = .1

def doubler(amount, days):
    for i in range(1, days):
        amount += round(MULTIPLIER * amount, 2)
    return amount

print(doubler(1, 180))
"""
class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(doubler(1, 2), 2)
    
    def test2(self):
        self.assertEqual(doubler(1, 4), 8)
    
    def test3(self):
        self.assertEqual(doubler(1, 5), 16)
    
    def test4(self):
        self.assertEqual(doubler(.01, 30), 5368709.12)
if __name__ == '__main__':
    unittest.main()"""