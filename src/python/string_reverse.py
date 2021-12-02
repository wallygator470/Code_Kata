import os

def main():
  screen_clear()
  test_function('hippopotamus', 'sumatopoppih')
  test_function('wally shoot', 'toohs yllaw')
  test_function('I love my life', 'efil ym evol I')
  test_function('racecar', 'racecar')

def string_reverse(string):
  return string[::-1]

def test_function(function_args, expected_result):
  print(string_reverse(function_args))
  assert(string_reverse(function_args)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()
