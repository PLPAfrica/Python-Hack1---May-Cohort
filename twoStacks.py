# a) Define the QueueWithStacks Class:

# -  Use two stacks (stack_in and stack_out) to simulate the queue behavior.
# -  stack_in will be used to handle the enqueue operations.
# -  stack_out will be used to handle the dequeue operations.

# b) Implement the 'enqueue' Method:

# -  Push the element onto stack_in.

# c) Implement the dequeue Method:

# -  If stack_out is empty, move all elements from stack_in to stack_out.
# -  Pop the top element from stack_out (which corresponds to the front element of the queue).

# d) Handle Edge Cases:

# -  Handle cases where dequeue is called on an empty queue by raising an exception.

# Pseudocode
# Class QueueWithStacks:
# __init__: Initialize two empty stacks (stack_in and stack_out).
# enqueue(x): Push x onto stack_in.
# dequeue() -> int:
# If stack_out is empty, move all elements from stack_in to stack_out.
# Pop and return the top element from stack_out.
# Raise an exception if both stacks are empty.

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

        if self.stack_out:
            return self.stack_out.pop()
        raise IndexError("dequeue from empty queue")


q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
