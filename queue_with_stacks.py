class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Attempting to pop from an empty stack")
    
    def is_empty(self):
        return len(self.items) == 0

class QueueWithStacks:
    def __init__(self):
        self.stack_in = Stack()  # Input stack
        self.stack_out = Stack()  # Output stack
    
    def enqueue(self, item: int):
        self.stack_in.push(item)
    
    def dequeue(self) -> int:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        
        if self.stack_out.is_empty():
            raise IndexError("Attempting to dequeue from an empty queue")
        
        return self.stack_out.pop()

# Example usage
if __name__ == "__main__":
    queue = QueueWithStacks()
    queue.enqueue(10)
    queue.enqueue(20)
    print(queue.dequeue()) 
     # Output: 10
    print(queue.dequeue()) 
     # Output: 20
