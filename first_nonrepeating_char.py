import os
from collections import Counter

def main():
  screen_clear()
  test_function('', '')
  test_function('a', 'a')
  test_function('oh my god dude where is my car', 'g')
  test_function('asdfsdafdasfjdfsafnnunlfdffvxcvsfansd', 'j')

def first_non_repeat(string):
  if string == '':
    return ''
  else:
    return [key for key, value in Counter(list(string)).items() if value == 1][0]

def test_function(function_args, expected_result):
  print(first_non_repeat(function_args))
  assert(first_non_repeat(function_args)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()