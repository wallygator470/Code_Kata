#import unittest

HAM = [2, 3, 5]

def hamming(n):
    count = 0
    number = 0
    while count < n:
        number += 1
        factors = (findFactors(number))
        if len(set(factors).difference(set(HAM))) > 0:
            next
        else:
            count += 1
        factorCounts = {factor:factors.count(factor) for factor in factors if factor in HAM}
        
    for num in HAM:
        if factorCounts.get(num) == None:
            factorCounts[num] = 0  

    return (2 ** factorCounts.get(2)) * (3 ** factorCounts.get(3)) * (5 ** factorCounts.get(5)) 
        
    
    
def findFactors(number):
    factors = []
    divisor = 2
    while number != 1:
        if number % divisor == 0:
            number = int(number / divisor)
            factors.append(divisor)
        else:
            divisor += 1
    return factors

print(hamming(500))

"""
class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(hamming(1), 2)
    
    def test2(self):
        self.assertEqual(hamming(2), 8)
    
    def test3(self):
        self.assertEqual(hamming(3), 16)
    
    def test4(self):
        self.assertEqual(hamming(4), 5368709.12)
if __name__ == '__main__':
    unittest.main()"""