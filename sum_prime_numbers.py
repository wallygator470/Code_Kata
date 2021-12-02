import os

def main():
  screen_clear()
  test_function(2, 2, 0, 2)
  test_function(3, 2, 0, 5)
  test_function(4, 2, 0, 5)
  test_function(5, 2, 0, 10)
  test_function(30, 2, 0, 129)
  test_function(55, 2, 0, 381)
  test_function(100, 2, 0, 1060)
  test_function(101, 2, 0, 1161)
  test_function(500, 2, 0, 21536)
  test_function(1000, 2, 0, 76127)
  test_function(10000, 2, 0, 5736396)

def sum_of_primes(n):
  prime_total = 0
  for num in range(1, n + 1):
    if num > 1:
      for i in range(2, n + 1):
        if (num % i) == 0 and num == i:
          prime_total += num
          break
        elif (num % i) == 0:
          break
  return prime_total

def recursive_sum_of_primes(n, c, t):
  # n = max end of ragne of numbers
  # c = where currently are at in the count from low to n
  # t = current total of prime numbers
  if c < n + 1:
    for i in range(2, n + 1):
      if (c % i) == 0 and c == i:
        t += c
        break
      elif (c % i) == 0:
        break
    c += 1
    return recursive_sum_of_primes(n, c, t)
  return t

def test_function(a, b, c, expected_result):
  s = sum_of_primes(a)
  print(s)
  assert(s) == expected_result
  if a <= 100:
    s = recursive_sum_of_primes(a, b, c)
    print(s)
    assert(s) == expected_result
  else:
    print('Too big for recursion')

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()