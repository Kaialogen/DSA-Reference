class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.length = 0

  def enqueue(self, element):
    new_node = Node(element)
    if self.rear is None:
      self.front = self.rear = new_node
      self.length += 1
      return
    self.rear.next = new_node
    self.rear = new_node
    self.length += 1

  def dequeue(self):
    if self.is_empty():
      return "Queue is empty"
    temp = self.front
    self.front = temp.next
    self.length -= 1
    if self.front is None:
      self.rear = None
    return temp.data

  def peek(self):
    if self.is_empty():
      return "Queue is empty"
    return self.front.data

  def is_empty(self):
    return self.length == 0

  def size(self):
    return self.length

  def print_queue(self):
    temp = self.front
    while temp:
      print(temp.data, end=" -> ")
      temp = temp.next
    print()

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", end="")
myQueue.print_queue()
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", end="")
myQueue.print_queue()
print("is_empty: ", myQueue.is_empty())
print("Size: ", myQueue.size())