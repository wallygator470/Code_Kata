import os

def main():
  screen_clear()
  test_function("racecar", True)
  test_function("taco cat", True)
  test_function("gold", False)
  test_function("A Santa Lived As a Devil At NASA", True)
  test_function("Wally", False)

def is_palindrome(string):
  return string.lower().replace(" ", "") == string[::-1].lower().replace(" ", "")

def test_function(function_args, expected_result):
  print(function_args, '=', is_palindrome(function_args))
  assert(is_palindrome(function_args)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()