def multiplier_of(mul):
    def multiplier(number):
        return number * mul
    return multiplier

multiplywith5 = multiplier_of(5)
multiplywith4 = multiplier_of(4)
multiplywith3 = multiplier_of(3)
multiplywith2 = multiplier_of(2)
print(multiplywith5(9))
print(multiplywith5(7))
print(multiplywith4(9))
print(multiplywith4(7))
print(multiplywith3(9))
print(multiplywith3(7))
print(multiplywith2(9))
print(multiplywith2(7))