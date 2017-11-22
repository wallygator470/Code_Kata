import unittest
from decimal import Decimal

class Calculator(object):
    
    def evaluate(self, string):
        parts = string.split()
        equation = []
        num = 0.
        pos = 0
        for i in range(len(parts) - pos):
            part = parts[i + pos]
            if part == "*":
                num *= Decimal(parts[i + pos + 1])
                pos += 1
                if i + pos + 1 == len(parts):
                    equation.append(num)
                    return float(sum(equation))
            elif part == "/":
                num /= Decimal(parts[i + pos + 1])
                pos += 1
                if i + pos + 1 == len(parts):
                    equation.append(num)
                    return float(sum(equation))
            elif part == "+":
                equation.append(num)
            elif part == "-":
                equation.append(num)
                parts[i + pos + 1] = str(Decimal(parts[i + pos + 1]) * -1)
            else:
                num = Decimal(part)
                if i + pos + 1 == len(parts):
                    equation.append(num)
                    return float(sum(equation))
            
#print(Calculator().evaluate("1.1 * 2.2 * 3.3"))

class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(Calculator().evaluate("10 + 5"), 15)
    
    def test2(self):
        self.assertEqual(Calculator().evaluate("10 - 5"), 5)
    
    def test3(self):
        self.assertEqual(Calculator().evaluate("10 * 5"), 50)
    
    def test4(self):
        self.assertEqual(Calculator().evaluate("10 / 5"), 2)
    
    def test5(self):
        self.assertEqual(Calculator().evaluate("10 / 5 - 9 / 3 + 13 * 5"), 64)
    
    def test6(self):
        self.assertEqual(Calculator().evaluate("1.1 + 2.2 + 3.3"), 6.6)
    
    def test7(self):
        self.assertEqual(Calculator().evaluate("1.1 * 2.2 * 3.3"), 7.986)
if __name__ == '__main__':
    unittest.main()