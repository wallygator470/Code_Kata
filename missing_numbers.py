import os

def main():
  screen_clear()
  test_function([0,1,3], [2])
  test_function([10,11,14,17], [12,13,15,16])
  test_function([3,7,9,19], [4,5,6,8,10,11,12,13,14,15,16,17,18])
  test_function([1,5,8,3,9,12], [2,4,6,7,10,11])
  test_function([88,2,2,3,2,93,4,6,7,93,94,95,96,98], [5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 89, 90, 91, 92, 97])

def missing_numbers(numbers):
    #return sorted(set(range(1, 101)) - set(number_list))
    numbers.sort()
    return sorted(set(range(numbers[0], numbers[-1])) - set(numbers))

def test_function(function_args, expected_result):
  print(missing_numbers(function_args))
  assert(missing_numbers(function_args)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()