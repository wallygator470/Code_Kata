import unittest

def nb_year(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years

""" my solution
def nb_year(p0, percent, aug, p):
    numYears = 0
    while p0 < p:
        numYears += 1
        p0 += (p0 * (percent / 100)) + aug
    
    print(numYears)
    return numYears
"""


class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(nb_year(1500, 5, 100, 5000), 15)
    
    def test2(self):
        self.assertEqual(nb_year(1500000, 2.5, 10000, 2000000), 10)
    
    def test3(self):
        self.assertEqual(nb_year(1500000, 0.25, 1000, 2000000), 94)
    
if __name__ == '__main__':
    unittest.main()