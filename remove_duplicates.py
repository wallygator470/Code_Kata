import os

def main():
  screen_clear()
  test_function([1,3,4,4,5,8,4,2,2], [1,3,4,5,8,2])
  test_function([3,5,6,9,9,4,3,12], [3,5,6,9,4,12])
  test_function([13,5,3,5,8,13,14,5,9], [13,5,3,8,14,9])
  test_function([8,8,15,6,19,7,12,6,6,3,13,9,15,14,1,13,4,11,16], [8,15,6,19,7,12,3,13,9,14,1,4,11,16])
  test_function([12,7,2,20,20,2,15,20,2,10,12,1], [12,7,2,20,15,10,1])
  test_function([6,12,5,1,4,18,10,17,10,0,1,7,6,18,11,2,15,19], [6,12,5,1,4,18,10,17,0,7,11,2,15,19])
  test_function([9,0,11,16,19,14,7,18,10,6,0,17,12,9,12,18,0,14,17], [9,0,11,16,19,14,7,18,10,6,17,12])
  test_function([5,10,3,17,9,12,19,4,16,19,7,9,7,8,10], [5,10,3,17,9,12,19,4,16,7,8])

def uniques(arr):
  new_nums = []
  for num in arr:
    if num not in new_nums:
      new_nums.append(num)
  return new_nums

def test_function(function_args1, expected_result):
  output = uniques(function_args1)
  print(output)
  assert(output) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()