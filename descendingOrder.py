import unittest

def Descending_Order(num): 
    print(int("".join(sorted(str(num), reverse=True))))
    return int("".join(sorted(str(num), reverse=True)))

class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(Descending_Order(0), 0)
    
    def test2(self):
        self.assertEqual(Descending_Order(15), 51)
    
    def test3(self):
        self.assertEqual(Descending_Order(123456789), 987654321)
    
    def test4(self):
        self.assertEqual(Descending_Order(1201), 2110)

if __name__ == '__main__':
    unittest.main()