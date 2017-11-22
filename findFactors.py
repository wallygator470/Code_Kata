import unittest
    
def findFactors(number):
    factors = []
    divisor = 2
    while number != 1:
        if number % divisor == 0:
            number = int(number / divisor)
            factors.append(divisor)
        else:
            divisor += 1
    print(factors)
    return factors

findFactors(6543)

class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(findFactors(2), [2])
    
    def test2(self):
        self.assertEqual(findFactors(4), [2, 2])
    
    def test3(self):
        self.assertEqual(findFactors(8), [2, 2, 2])
    
    def test4(self):
        self.assertEqual(findFactors(13), [13])
    
    def test5(self):
        self.assertEqual(findFactors(35), [5, 7])

if __name__ == '__main__':
    unittest.main()