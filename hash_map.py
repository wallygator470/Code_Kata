import os

def main():
  screen_clear()
  d = Hashmap()
  d.set("jess", "213-559-6840")
  print(dict(d))
  d.set("james", "123-456-7890")
  print(dict(d))
  print (d.get("james"))
 
class Node:

  def __init__(self, key, value):
    self.key = key
    self.value = value

class Hashmap:

  def __init__(self):
    self.storage = [None for _ in range(16)]
    self.size = 0

  def position(self, key_hash):
    return key_hash % 16

  def hashStr(self, key):
    if isinstance(key, int):
      return key
    result = 5381
    for char in key:
      result = 33 * result + ord(char)
    return result

  def set(self, key, val):
    p = Node(key, val)
    key_hash = self.hashStr(key)
    index = self.position(key_hash)
    if not self.storage[index]:
      self.storage[index] = [p]
      self.size += 1
    else:
      list_at_index = self.storage[index]
      if p not in list_at_index:
        self.storage[index] = [p]
        self.size += 1
      else:
        for i in list_at_index:
          if i == p:
            i.value = val
            break

  def get(self, key):
    key_hash = self.hashStr(key)
    index = self.position(key_hash)
    if not self.storage[index]:
      return None
    else:
      list_at_index = self.storage[index]
      for i in list_at_index:
        if i.key == key:
          return i.value
    return None

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()
