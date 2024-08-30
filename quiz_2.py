class QueueWithStacks:
    def __init__(self):
        # Initializing two stacks 
        self.stack_in = []
        self.stack_out = []
    
    def enqueue(self, x: int):
        # Pushing  the element onto stack_in
        self.stack_in.append(x)
    
    def dequeue(self) -> int:
        # If stack_out is empty, transfer elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        # If stack_out is still empty, the queue is empty
        if not self.stack_out:
            raise IndexError("Dequeue from an empty queue")
        
        # Pop the element from stack_out
        return self.stack_out.pop()


q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Outputs  1
print(q.dequeue())  # Outputs 2
