import unittest

def convertFracts(fractionList):
    newFractionList = []
    commonDen = getCommonDenominator(removeSubFactors(getDivisors(fractionList)))
    #comDen = 
    for fraction in fractionList:
        newFractionList.append(createNewFraction(fraction, commonDen))
    print(newFractionList)
    return newFractionList

def getGCD(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def getLCM(a, b):
    """Return lowest common multiple."""
    return a * b // getGCD(a, b)

def getDivisors(fractionList):
    print([divisor[1] for divisor in fractionList])
    return [divisor[1] for divisor in fractionList] 

def removeSubFactors(numbers):
    countNumbers = len(numbers)
    newList = []
    for number in numbers:
        for i in range(countNumbers):
            if numbers[i] == number and i + 1 != countNumbers:
                next
            elif i + 1 == countNumbers:
                newList.append(number)
            elif numbers[i] % number == 0:
                break
            else:
                next
    print(newList)
    return newList

def reduceDivisor(number, divisors):
    for divisor in divisors:
        factors = getFactors(divisor)
        for factor in factors:
            if number % factor == 0 and number / factor % divisor == 0:
                number /= factor
    print(number)
    return int(round(number))

def getFactors(number):
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

def getCommonDenominator(divisors):
    if len(divisors) == 1:
        print(divisors[0])
        return divisors[0]
    else:
        print(reduceDivisor(eval(str(tuple(divisors)).replace(',','*')), divisors))
        return reduceDivisor(eval(str(tuple(divisors)).replace(',','*')), divisors)

def createNewFraction(fraction, commonDen):
    print(int(commonDen / fraction[1]) * fraction[0])
    return [(int(commonDen / fraction[1]) * fraction[0], commonDen)]


class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(convertFracts([[1, 2], [1, 3], [1, 4]]), [[6, 12], [4, 12], [3, 12]])

if __name__ == '__main__':
    unittest.main()
