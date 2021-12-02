import os

def main():
  screen_clear()
  test_function([3, 4, 2, 5], 6)
  test_function([1, 3, 2, 6, 5, 4], 9)

def max_of_min_pairs(nums):
  s = 0
  nums.sort()
  k = len(nums)
  i = 0
  while(i < k):
    s += nums[i]
    i += 2
  return s

def test_function(function_args, expected_result):
  print(max_of_min_pairs(function_args))
  assert(max_of_min_pairs(function_args)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()