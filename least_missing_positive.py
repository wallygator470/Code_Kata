import os

def main():
  screen_clear()
  test_function([1, 2, 3, 0], 4)
  test_function([0, 3, -1, -2, 1], 2)
  test_function([-5,-6,-7,-8,-9], 1)
  test_function([0, 3, -1, -3, 1], 2)
  test_function([5,6,7,8,9], 1)
  test_function([], 1)

def least_missing_pos(nums):
  k = 0
  c = 0
  n = len(nums)
  nums.sort()
  if n == 0:
    return 1
  else:
    while(k < n - 1):
      c = nums[k]
      if (nums[0] != 1 and nums[0] > 0) or nums[-1] <= 0:
        return 1
      elif c + 1 != nums[k + 1] and c + 1 > 0:
        return c + 1
      k += 1
  return c + 2

def test_function(function_args1, expected_result):
  output = least_missing_pos(function_args1)
  print(output)
  assert(output) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()