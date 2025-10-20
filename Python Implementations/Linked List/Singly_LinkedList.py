class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.first = None

  def is_empty(self):
    return self.first is None

  def add_to_front(self, value):
    fresh_node = Node(value)
    fresh_node.next = self.first
    self.first = fresh_node

  def add_to_end(self, value):
    fresh_node = Node(value)
    
    # Handle empty list case
    if self.is_empty():
        self.first = fresh_node
        return
        
    # Navigate to the last element
    current_element = self.first
    while current_element.next:
        current_element = current_element.next
        
    # Connect the new node at the end
    current_element.next = fresh_node

my_linked_list = LinkedList();

my_linked_list.add_to_end(20)
my_linked_list.add_to_end(30)