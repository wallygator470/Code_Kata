import os

FIZZ = 3
BUZZ = 5

def main():
  screen_clear()
  print(str(fizz_buzz(0)))
  print("\n")
  print(str(fizz_buzz(1)))
  print("\n")
  print(str(fizz_buzz(15)))
  print("\n")
  print(str(fizz_buzz(34)))
  print("\n")
  print(str(fizz_buzz(100)))
  print("\n")
  print(str(fizz_buzz(1000)))
  print("\n")

def fizz_buzz(num):
  final_arr = []
  for i in range(1, num + 1):
    if i % FIZZ == 0 and i % BUZZ == 0:
      final_arr.append("fizzbuzz")
    elif i % FIZZ == 0:
      final_arr.append("fizz")
    elif i % BUZZ == 0:
      final_arr.append("buzz")
    else:
      final_arr.append(str(i))
  return "".join(final_arr)

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()