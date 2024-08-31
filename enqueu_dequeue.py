class QueueWithStacks:
    def __init__(self):
        self.stack_in = []  # Stack for enqueue operations
        self.stack_out = []  # Stack for dequeue operations

    def enqueue(self, x: int):
        self.stack_in.append(x)  # Simply push the element to stack_in

    def dequeue(self) -> int:
        # If stack_out is empty, move all elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        # Pop and return the top element from stack_out
        if self.stack_out:
            return self.stack_out.pop()
        else:
            raise IndexError("Queue is empty")

# Example usage
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  
print(q.dequeue())  
