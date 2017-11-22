import unittest

def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

""" my solution
    total = 0
    for i in range(number):
        if i % 5 == 0 or i % 3 == 0:
            total += i
    
    return total
"""

    

class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(solution(10), 23)
    
    def test2(self):
        self.assertEqual(solution(11), 33)
    
    def test3(self):
        self.assertEqual(solution(13), 45)

if __name__ == '__main__':
    unittest.main()