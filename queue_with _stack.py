class QueueWithStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x: int):
        self.stack_in.append(x)

    def dequeue(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("dequeue from empty queue")
        return self.stack_out.pop()

# Example usage:
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
