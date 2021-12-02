import os
from is_palindrome import is_palindrome

MULTIPLIER = 10

def main():
  #test_function([2,4,3], [5,6,4], )
  #test_function([0], [0], )
  #test_function([9,9,9,9,9,9,9,9,9,8], [9,9,9,9], )
  test_function(195, 9339)
  test_function(265, 45254)
  test_function(196, 'None')

def reverse_add(num):
  num = num + int(''.join(str(num)[::-1]))
  if num < 4294967295:
    if is_palindrome(str(num)) == True:
      return num
    else:
      return reverse_add(num)
  else:
    return 'None'

# def is_palindrome(num):
#   if num == int(''.join(str(num)[::-1])):
#     return True
#   else:
#     return False

#def reverse_add(n1, n2):
#  num1 = add_list(n1)
#  num2 = add_list(n2)
#  return make_list(num1 + num2)

def add_list(nums):
  total = 0
  pos = 1
  for num in nums:
    total += (num * pos)
    pos *= MULTIPLIER
  return total
  #return [n * pos, pos * MULTIPLIER for n in nums][0]

def make_list(num):
  return list(int(n) for n in str(num)[::-1])

def test_function(function_args1, expected_result):
  output = reverse_add(function_args1)
  print(output)
  assert(output) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()
