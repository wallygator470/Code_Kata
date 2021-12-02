import os
product = 0

def main():
  screen_clear()
  test_function([], 0)
  test_function([0, 1, 2, 3], 6)
  test_function([-12, -7, -1, 11, 17], 1428)
  test_function([0, 4, -9, 19, 7, -5], 855)
  test_function([-1, 9, 22, 3, -15, -7], 2310)

def max_product_of_three(nums):
  global product
  i = 0
  l = len(nums)
  if l == 0:
    largest_product = product
    product = 0
    return largest_product
  else:
    while(i < l - 2):
      j = i + 1
      while(j < l):
        k = j + 1
        while(k < l):
          new_product = nums[i] * nums[j] * nums[k]
          if new_product > product:
            product = new_product
          k += 1
        j += 1
      i += 1
    nums.pop(0)
    return max_product_of_three(nums)

def max_product_of_three_orig(nums):
  product = 0
  i = 0
  l = len(nums)
  if l == 0:
    return product
  else:
    while(i < l - 2):
      j = i + 1
      while(j < l):
        k = j + 1
        while(k < l):
          new_product = nums[i] * nums[j] * nums[k]
          if new_product > product:
            product = new_product
          k += 1
        j += 1
      i += 1
    return product

def test_function(a1, e):
  output = max_product_of_three_orig(a1)
  print(output)
  assert(output) == e
  output = max_product_of_three(a1)
  print(output)
  assert(output) == e

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()