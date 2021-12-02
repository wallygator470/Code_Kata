import os

def main():
  screen_clear()
  test_function([1, 9, 13, 20, 47], 10, [0, 1])
  test_function([3, 2, 4, 1, 9], 12, [0, 4])
  test_function([], 10, [])
  test_function([3, 2, 4, 1, 9], 13, [2, 4])
  test_function([1, 9, 13, 20, 47], 29, [1, 3])
  test_function([3, 2, 4, 1, 9], 6, [1, 2])

def two_sum(nums, result):
  if len(nums) == 0:
    return []
  else:
    for num in nums:
      for other_num in nums:
        a = nums.index(num)
        b = nums.index(other_num)
        if a == b:
          continue
        else:
          print('num:', num, 'other_num:', other_num)
          if num + other_num == result:
            return [nums.index(num), nums.index(other_num)]

def test_function(function_args1, function_args2, expected_result):
  output = two_sum(function_args1, function_args2)
  print(output)
  assert(output) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()