import os

def main():
  screen_clear()
  test_function(1, 1)
  test_function(2, 1)
  test_function(3, 2)
  test_function(4, 3)
  test_function(5, 5)
  test_function(17, 1597)
  test_function(34, 5702887)

def fibonacci(num):
  if num < 0:
    print('Invalid Input')
  elif num == 0:
    return 0
  elif num <= 2:
    return 1
  else:
    return fibonacci(num - 1) + fibonacci(num - 2)

def fibonacci_normal(num):
  a = 0
  b = 1
  s = 0
  if num < 0:
    print('Invalid Input')
  elif num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    for i in range(1, num):
      s = a + b
      a = b
      b = s
    return b

def fibonacci_dynamic(num):
  fib_array = [0, 1]
  # Check if num is less than 0
  if num <= 0:
    print('Invalid Input')
  # Check if num is less than len(fib_array)
  elif num < len(fib_array):
    return fib_array[num]
  elif num == len(fib_array):
    return fib_array[num - 1]
  else:
    temp_fib = fibonacci(num - 1) + fibonacci(num - 2)
    fib_array.append(temp_fib)
    return temp_fib

def test_function(a1, e):
  # a1 = first argument
  # e = expected result
  s = fibonacci(a1)
  print(s)
  assert(s) == e
  s = fibonacci_normal(a1)
  print(s)
  assert(s) == e
  s = fibonacci_dynamic(a1)
  print(s)
  #assert(s) == e

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()