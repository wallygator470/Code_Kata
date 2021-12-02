MIN = 0
MAX = 100

fst_div = 3
sec_div = 11

for i in range(MIN, MAX):
    num = i + 1
    if num % fst_div == 0 and num % sec_div == 0:
        print("FizzBuzz")
    elif num % fst_div == 0:
        print("Fizz")
    elif num % sec_div == 0:
        print("Buzz")
    else: 
        print (num)
    
    
