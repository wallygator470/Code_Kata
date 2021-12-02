import os

def main():
  screen_clear()
  test_function(49, 4)
  test_function(1, 1)
  test_function(439230, 3)
  test_function(49651648911, 9)

def sum_digits(num):
  num = sum([int(d) for d in str(num)])
  if len(str(num)) == 1:
    return num
  else:
    return sum_digits(num)

def test_function(function_args, expected_result):
  print(sum_digits(function_args))
  assert(sum_digits(function_args)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()
