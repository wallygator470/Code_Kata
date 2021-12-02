import os

def main():
  screen_clear()
  test_function('silent', 'listen', True)
  test_function('fairy tales', 'safety rail', True)
  test_function('help me', 'listen', False)
  test_function('Mary', 'Army', True)
  test_function('cinema', 'iceman', True)
  test_function('jake', 'jay', False)

def is_anagram(string1, string2):
  return sorted(string1.lower()) == sorted(string2.lower())

def test_function(function_arg1, function_arg2, expected_result):
  print(is_anagram(function_arg1, function_arg2))
  assert(is_anagram(function_arg1, function_arg2)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()