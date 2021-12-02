import os
from collections import Counter

def main():
  screen_clear()
  test_function([4, 4, 6, 1, 3, 1, 3], 6)

def lonelyNumber(numbers):
  counts = Counter(numbers)
  return (min(counts, key = counts.get), counts.get(max(counts, key = counts.get)))[0]

def test_function(function_args, expected_result):
  print(lonelyNumber(function_args))
  assert(lonelyNumber(function_args)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()
