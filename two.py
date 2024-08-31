class QueueWithStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueue operations
        self.stack2 = []  # Stack for dequeue operations
    
    def enqueue(self, x: int):
        
        # Add the element to stack1
        self.stack1.append(x)
    
    def dequeue(self) -> int:
        if not self.stack2:
            
            # If stack2 is empty, move elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if self.stack2:
            
            # Pop and return the top element of stack2, which is the front of the queue
            return self.stack2.pop()
        else:
            
            # If both stacks are empty, raise an exception (queue is empty)
            raise IndexError("dequeue from empty queue")

q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
