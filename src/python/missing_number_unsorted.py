import os

def main():
  screen_clear()
  test_function([2,5,1,4,9,6,3,7], 1, 9, 8)
  test_function([2,5,1,4,8,6,3,7], 1, 9, 9)
  test_function([2,5,8,4,9,6,3,7], 1, 9, 1)

def missing_in_unsorted(arr, lower_bound, upper_bound):
    arr.sort()
    if arr[-1] != upper_bound:
      return upper_bound
    else:
      k = lower_bound - 1
      for num in arr:
        if num != lower_bound + k:
          return lower_bound + k
        k += 1

def test_function(a, b, c, expected_result):
  print(missing_in_unsorted(a, b, c))
  assert(missing_in_unsorted(a, b, c)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()