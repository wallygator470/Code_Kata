import os

def main():
  screen_clear()
  test_function([], [])
  test_function([1,2,3], [6,3,2])
  test_function([1, 2, 4, 16], [128,64,32,8])
  test_function([7,8,5,18,16,11,20], [2534400,2217600,3548160,985600,1108800,1612800,887040])
  test_function([9,9,3,4,18,8,6,18,1,6,19], [191476224,191476224,574428672,430821504,95738112,215410752,287214336,95738112,1723286016,287214336,90699264])

def product_except_self(nums):
  products = []
  if nums == products:
    return products
  else:
    for i in range(len(nums)):
      products.append(get_product(nums, i))
    return products

def get_product(nums, i):
  result = 1
  k = 0
  for num in nums:
    if i == k:
      k += 1
    else:
      result *= num
      k += 1
  return result

def test_function(function_args1, expected_result):
  output = product_except_self(function_args1)
  print(output)
  assert(output) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()