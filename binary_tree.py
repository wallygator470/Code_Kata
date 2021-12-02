import os

def main():
  # Driver code
  root = Node(5)
  root.left = Node(10)
  root.right = Node(8)
  root.left.left = Node(17)
  root.left.right = Node(3)
  print("Preorder traversal of binary tree is")
  preorder(root)
  print("\nInorder traversal of binary tree is")
  inorder(root)
  print("\nPostorder traversal of binary tree is")
  postorder(root)

  # root = Node(17)
  # root.left = Node(3)
  # root.right = Node(10)
  # root.left.left = Node(5)
  # root.left.right = Node(8)
  # #root = [17, 10, 3, 5, 8]
  # print(inorder(root))
  # print(postorder(root))
  # print(inorder(root))

class Node:
  def __init__(self,key):
    self.left = None
    self.right = None
    self.val = key

def inorder(root):
  if root:
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def postorder(root):
  if root:
    postorder(root.left)
    postorder(root.right)
    print(root.val)

def preorder(root):
  if root:
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# clears the screen based on your type of computer
def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()
