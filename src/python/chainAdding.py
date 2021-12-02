import unittest

class add(int):
    def __call__(self, val):
        return type(self)(self + val)

class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(add(1), 1)
    
    def test2(self):
        self.assertEqual(add(1)(2), 3)
    
if __name__ == '__main__':
    unittest.main()