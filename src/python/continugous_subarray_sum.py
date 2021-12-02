import os

def main():
  screen_clear()
  test_function([], 3, False)
  test_function([1,2,3], 3, True)
  test_function([1,2,3], 5, True)
  test_function([1,2,3], 3, True)
  test_function([1,2,3], 6, True)
  test_function([1,2,3,4], 11, False)
  test_function([3, 6, 12, 35], 47, True)

def subarray_sum(nums, n):
  if len(nums) == 0:
    return False
  else:
    t = 0
    for num in nums:
      t = t + num
      if t == n:
        return True
    nums.pop(0)
    return subarray_sum(nums, n)

def test_function(function_args1, function_args2, expected_result):
  output = subarray_sum(function_args1, function_args2)
  print(output)
  assert(output) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()