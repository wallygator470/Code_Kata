import os

def main():
  screen_clear()
  test_function('sea!$hells3', 'sll!$ehaes3')
  test_function('hipp!op28ota(mus', 'suma!to28pop(pih')
  test_function('wally$$ sh00t', 'thsyl$$ la00w')
  test_function('1kas90jda3', '1adj90sak3')

def reverse_alpha(string):
  new_char_list = []
  char_list = list(string)
  for char in char_list:
    if char.isalpha():
      new_char_list.append(char)
  new_char_list.reverse()
  char_list = []
  i = 0
  for char in list(string):
    if char.isalpha():
      char_list.append(new_char_list[i])
      i += 1
    else:
      char_list.append(char)
  return "".join(char_list)

def test_function(function_args, expected_result):
  print(reverse_alpha(function_args))
  assert(reverse_alpha(function_args)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()
