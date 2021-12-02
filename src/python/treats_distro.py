import os
from collections import Counter

def main():
  screen_clear()
  test_function([2, 2, 3, 3, 4, 4], 3)
  test_function([1, 1, 2, 4], 2)
  test_function([7,7], 1) # online example says this is = 2, but I cannot see why it would be there is only one unique snack and two of them.

def treats_distribution(snacks):
  return int(sum(list(Counter(snacks).values()))/2)

def get_counts(nums):
  return Counter(nums)

def test_function(function_args1, expected_result):
  output = treats_distribution(function_args1)
  print(output)
  assert(output) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()