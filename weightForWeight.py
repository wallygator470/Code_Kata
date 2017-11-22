import unittest

def order_weight(strng):
    return " ".join(sorted(sorted(strng.split()), key=sumWeight))

def sumWeight(weight):
    return sum(int(weight[pos]) for pos in range(len(weight)))
    
class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
    
    def test2(self):
        self.assertEqual(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
    
if __name__ == '__main__':
    unittest.main()