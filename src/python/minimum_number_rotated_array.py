import os

def main():
  screen_clear()
  test_function([6, 7, 8, 0, 1, 2, 3, 4, 5], 0)
  test_function([6, 7, 8, 9, 10, 3, 4, 5], 3)

def get_minimum(nums):
  nums.sort()
  return nums[0]

def test_function(a, e):
  # a = first argument
  # e = expected result
  s = get_minimum(a)
  print(s)
  assert(s) == e

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()