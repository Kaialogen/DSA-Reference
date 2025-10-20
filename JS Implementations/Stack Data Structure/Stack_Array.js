class Stack {
  constructor() {
    this.items = [];
  }
  push(item) {
    this.items.push(item);
  }
  pop() {
    if (this.items.length === 0) {
      return null;
    }
    return this.items.pop();
  }
  peek() {
    if (this.items.length === 0) {
      return null;
    }
    return this.items[this.items.length - 1];
  }
  isEmpty() {
    return this.items.length === 0;
  }
  size() {
    return this.items.length;
  }
}

const stack = new Stack();
stack.push(3);
stack.push(5);
console.log(stack.peek()); // 5
console.log(stack.pop()); // 5
console.log(stack.isEmpty()); // false
