import os

def main():
  screen_clear()
  test_function([1,2,2,1], [2,2], [2])
  test_function([4,9,5], [9,4,9,8,4], [9,4])

def intersection_orig(nums1, nums2):
  intersect_nums = []
  for num2 in dedupe(nums2):
    if num2 in dedupe(nums1):
      intersect_nums.append(num2)
  return intersect_nums

def dedupe(nums):
  return list(set(nums))

def intersection(nums1, nums2):
  nums1 = set(nums1)
  nums2 = set(nums2)
  return list(nums1.intersection(nums2))

def test_function(function_args1, function_args2, expected_result):
  print('Original', intersection_orig(function_args1, function_args2))
  assert(intersection_orig(function_args1, function_args2)) == expected_result
  print('New', intersection(function_args1, function_args2))
  assert(intersection(function_args1, function_args2)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()