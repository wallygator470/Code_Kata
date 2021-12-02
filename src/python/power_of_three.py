import os

def main():
  screen_clear()
  test_function(9, True)
  test_function(7, False)
  test_function(18, True)
  test_function(600, True)
  test_function(81, True)
  test_function(729, True)
  test_function(15, True)
  test_function(16, False)

def power_of_three(num):
  if num % 3 == 0:
    return True
  else:
    return False

def test_function(function_args, expected_result):
  print(power_of_three(function_args))
  assert(power_of_three(function_args)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()
