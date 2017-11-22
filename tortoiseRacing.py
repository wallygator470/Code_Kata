import unittest

def race(v1, v2, g):
    if v2 < v1:
        return None
    time = (g * 3600 / (v2 - v1))
    return [int(time / 3600), int(time % 3600 / 60), int(time % 60)]

class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(race(720, 850, 70), [0, 32, 18])

    def test2(self):
        self.assertEqual(race(80, 91, 37), [3, 21, 49])
    
    def test3(self):
        self.assertEqual(race(80, 100, 40), [2, 0, 0])
    
    def test4(self):
        self.assertEqual(race(0, -44, -39), None)
    
if __name__ == '__main__':
    unittest.main()