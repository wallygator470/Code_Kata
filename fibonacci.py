import unittest
import types
import cmath

dicFib = { 0:0 ,1 :1 }
iterations = 0

def fib(x):
    if type(cal_fib()) == types.GeneratorType:
        counter = 0
        for number in cal_fib():
            if counter == abs(x):
                if x < 0 and x % 2 == 0:
                    return number * -1
                else:
                    return number
            counter += 1

def cal_fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

def fib2(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

def fib3(n):
    a, b = 0, 1
    while n:
        a, b, n = b, a + b, n - 1
    return a

def fib4(n):
    if  (n in dicFib):      
        return dicFib[n]    
    else :
        global iterations               
        fib = fib4(n - 2) + fib4(n - 1)
        dicFib[n] = fib
        iterations += 1
        return fib

def fib5(n):
    lsa = (1 / cmath.sqrt(5)) * pow(((1 + cmath.sqrt(5)) / 2), n)
    rsa = (1 / cmath.sqrt(5)) * pow(((1 - cmath.sqrt(5)) / 2), n)
    fib = lsa-rsa
    #coerce to real so we can round the complex result
    fn = round(fib.real) 
    return fn 

def fib6(n):
    if n < 0 and n % 2 == 0:
        return _fib(abs(n))[0] * (-1)
    else:
        return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

"""
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(5))
print(fib(-6))
print(fib(-13))"""
print(fib6(100000))
"""
class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(fib(0), 0)
    
    def test2(self):
        self.assertEqual(fib(1), 1)
    
    def test3(self):
        self.assertEqual(fib(2), 1)
    
    def test4(self):
        self.assertEqual(fib(3), 2)
    
    def test5(self):
        self.assertEqual(fib(4), 3)
    
    def test6(self):
        self.assertEqual(fib(5), 5)
    
    def test7(self):
        self.assertEqual(fib(6), 8)
    
    def test8(self):
        self.assertEqual(fib(-6), -8)
    
    def test9(self):
        self.assertEqual(fib(-13), 233)
    
if __name__ == '__main__':
    unittest.main()"""