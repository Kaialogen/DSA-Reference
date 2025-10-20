class Queue:
  def __init__(self):
    self.queue = []
    
  def enqueue(self, element):
    self.queue.append(element)

  def dequeue(self):
    if self.is_empty():
      return "Queue is empty"
    return self.queue.pop(0)

  def peek(self):
    if self.is_empty():
      return "Queue is empty"
    return self.queue[0]

  def is_empty(self):
    return len(self.queue) == 0

  def size(self):
    return len(self.queue)

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", myQueue.queue)
print("is_empty: ", myQueue.is_empty())
print("Size: ", myQueue.size())