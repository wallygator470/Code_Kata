import os

def main():
  screen_clear()
  test_function('twocan', 'two', 0)
  test_function('thepigflewwow', 'flew', 6)
  test_function('thepigflewwow', 'felw', -1)
  test_function('wherearemyshorts', 'pork', -1)

def detectSubstring(phrase, string):
  return phrase.find(string)

def test_function(function_args1, function_args2, expected_result):
  print(detectSubstring(function_args1, function_args2))
  assert(detectSubstring(function_args1, function_args2)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()