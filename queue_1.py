class QueueWithStacks:
    def __init__(self):
        # Initialize two stacks
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x: int):
        # Push element onto the stack_in
        self.stack_in.append(x)

    def dequeue(self) -> int:
        # If stack_out is empty, transfer all elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        # If stack_out is still empty after the transfer, the queue is empty
        if not self.stack_out:
            return None  # or raise an exception if preferred

        # Pop and return the front element
        return self.stack_out.pop()

# Example usage:
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
