class QueueWithStacks:
    def __init__(self):
        self.stack_in = []  # Stack for incoming items
        self.stack_out = []  # Stack for outgoing items

    def enqueue(self, x: int):
        self.stack_in.append(x)

    def dequeue(self) -> int:
        if not self.stack_out:
            # Move items from stack_in to stack_out, reversing their order
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            return self.stack_out.pop()
        else:
            raise IndexError("dequeue from an empty queue")  # Handle empty queue

# Usage
q = QueueWithStacks()
q.enqueue(15)
q.enqueue(20)
q.enqueue(25)

print(q.dequeue())  # Output: 15
print(q.dequeue())  # Output: 20

print()

q.enqueue(30)
q.enqueue(35)

print(q.dequeue())  # Output: 25
print(q.dequeue())  # Output: 30