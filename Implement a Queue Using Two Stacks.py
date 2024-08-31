class QueueWithStacks:
    def __init__(self):
        # Initialize two stacks
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, x: int):
        # Push the element onto stack1
        self.stack1.append(x)
    
    def dequeue(self) -> int:
        # If stack2 is empty, transfer elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, the queue is empty
        if not self.stack2:
            raise IndexError("Dequeue from an empty queue")
        
        # Pop the top element from stack2
        return self.stack2.pop()
