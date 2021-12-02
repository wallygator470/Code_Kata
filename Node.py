class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

  def get_data(self):
    return self.data

  def get_next(self):
    return self.next

  def set_next(self, new_next):
    self.next = new_next