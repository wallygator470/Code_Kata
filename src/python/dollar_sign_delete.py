import os

FIRST_ELEMENT = 0
SECOND_ELEMENT = 1

def main():
  screen_clear()
  test_function(["f$ec", "ec"], True)
  test_function(["a90$n$c$se", "a90n$cse"], False)
  test_function(['ab$$', 'c$d$'], True)
  test_function(['b$$p', '$b$p'], True)
  test_function(['$$bp', '$b$p'], False)

def is_dollar_delete_equal(two_element_list):
  return delete_dollar(two_element_list[FIRST_ELEMENT]) == delete_dollar(two_element_list[SECOND_ELEMENT])

def delete_dollar(string):
  str_list = list(string)
  for c in str_list:
    b = str_list.index(c)
    if str_list.index(c) == FIRST_ELEMENT and c == '$':
      str_list.pop(b)
      string = ''.join(str_list)
      return delete_dollar(string)
    elif c == '$':
      b -= 1
      str_list.pop(b)
      str_list.pop(b)
      string = ''.join(str_list)
      return delete_dollar(string)
  string = ''.join(str_list)
  return string

def test_function(function_args, expected_result):
  print(is_dollar_delete_equal(function_args))
  assert(is_dollar_delete_equal(function_args)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()