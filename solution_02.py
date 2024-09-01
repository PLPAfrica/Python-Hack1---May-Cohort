class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

class QueueWithStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()  

    def enqueue(self, x: int):
        self.stack1.push(x)

    def dequeue(self) -> int:
        if self.stack1.is_empty() and self.stack2.is_empty():
            raise IndexError("Queue is empty")
        
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.pop()

# Test
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue()) 
print(q.dequeue())