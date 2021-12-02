import os

def main():
  screen_clear()
  test_function([[1, 4], [2, 5], [7, 10], [12, 16]], [[1, 5], [7, 16]])

def merge_intervals(ranges):
  ranges.sort()
  new_ranges = []
  for rng in ranges:
    new_range = rng.copy()
    ranges.pop(0)
    for cur_rng in ranges:
      new_range.sort()
      new_range.sort()
      cur_rng.sort()
      if (new_range[1] >= cur_rng[0]):
        if (new_range[1] <= cur_rng[1]):
          new_range[1] = cur_rng[1]
          ranges.pop(0)
        else:
          ranges.pop(0)
      if (len(ranges) == 2 and new_range[1] != cur_rng[1]):
        new_ranges.append(cur_rng)
      new_ranges.append(new_range)
    new_ranges.sort()
    return list(set(new_ranges))

def test_function(function_args, expected_result):
  print(merge_intervals(function_args))
  assert(merge_intervals(function_args)) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')
main()