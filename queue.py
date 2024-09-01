class QueueWithStacks:
    def __init__(self):
        # Initialize two stacks
        self.stack_in = []   # Stack for enqueue operations
        self.stack_out = []  # Stack for dequeue operations

    def enqueue(self, x: int):
        # Push the new element onto the input stack
        self.stack_in.append(x)

    def dequeue(self) -> int:
        # If the output stack is empty, transfer elements from input stack
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        # If the output stack is still empty, raise an error
        if not self.stack_out:
            raise IndexError("dequeue from empty queue")

        return self.stack_out.pop()

q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.dequeue())