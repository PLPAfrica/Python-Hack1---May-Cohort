class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0

class QueueWithStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def enqueue(self, x: int):
        self.stack1.push(x)
    
    def dequeue(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

# Example usage:
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(10)
    q.enqueue(20)
    print(q.dequeue())  
    print(q.dequeue())  
