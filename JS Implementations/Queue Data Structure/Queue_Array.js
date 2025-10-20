class Queue {
  constructor() {
    this.items = [];
  }

  // Add an element to the end of the queue
  enqueue(item) {
    this.items.push(item);
  }

  // Remove and return the element at the front of the queue
  dequeue() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items.shift(); // shift removes the first element
  }

  // View the element at the front without removing it
  peek() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items[0];
  }

  // Check if the queue is empty
  isEmpty() {
    return this.items.length === 0;
  }

  // Return the number of elements in the queue
  size() {
    return this.items.length;
  }
}

// Example usage:
const queue = new Queue();
queue.enqueue(10);
queue.enqueue(20);
console.log(queue.peek()); // 10
console.log(queue.dequeue()); // 10
console.log(queue.size()); // 1
