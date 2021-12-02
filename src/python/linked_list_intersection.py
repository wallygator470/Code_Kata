import os
#import Node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def main():
  screen_clear()

  list1 = Node(3)
  nodes1 = [4,5,6,7,8,9,10]
  create_nodes(list1, nodes1)
  print(nodes1)

  list2 = Node(1)
  nodes2 = [2,3,4,5,6,7,8]
  create_nodes(list2, nodes2)
  print(nodes2)

  test_function(list1, list2, '345678')

def get_intersection(list1, list2):
  c1 = get_count(list1)
  c2 = get_count(list2)
  if c1 > c2:
    d = c1 - c2
    return get_node(d, list1, list2)
  else:
    d = c2 - c1
    return get_node(d, list2, list1)

def get_node(d, node1, node2):
  cur1 = node1
  cur2 = node2
  for i in range(d):
    if cur1 == None:
      return -1
    cur1 = cur1.next
  while cur1 != None and cur2 != None:
    if cur1.data == cur2.data:
      return cur1.data
    cur1 = cur1.next
    cur2 = cur2.next
  return -1

def get_count(node):
  current = node
  count = 0
  while current != None:
    count += 1
    current = current.next
  return count

def create_nodes(head, nodes):
  for val in nodes:
    print(val)
    new_node = Node(val)
    head.next = new_node
    print(head.next)
    head = new_node
    print(head)

def list_to_str(head):
  new_str = ""
  while head:
    new_str += str(head.val)
    head = head.next
  return new_str

def test_function(function_args1, function_args2, expected_result):
  output = get_intersection(function_args1, function_args2)
  print(output)
  #assert(output) == expected_result

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()