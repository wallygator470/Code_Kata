import os
from collections import Counter

def main():
  screen_clear()
  test_function([4, 2, 4], 4)
  test_function([4, 2, 4, 2], None)
  test_function([4, 2, 4, 2, 1, 4, 1, 2, 4], None)
  test_function([1, 4, 2, 4, 4, 3, 4], 4)
  test_function([1, 1, 1, 4, 2, 4, 4, 3, 1, 1, 1], 1)

def majority_element(nums):
  k_v = get_highest_count(nums)
  if get_percentage(k_v[1], len(nums)) > .5:
    return k_v[0]

def get_highest_count(nums):
  counts = Counter(nums)
  return (max(counts, key = counts.get), counts.get(max(counts, key = counts.get)))

def get_percentage(cnt, num):
  return cnt / num

def test_function(function_args, expected_result):
  print(majority_element(function_args))
  assert(majority_element(function_args)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()
