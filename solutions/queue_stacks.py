class QueueWithStacks:
    """
    A queue implementation using two stacks.
    """

    def __init__(self):
        self.stack_in = []  # Stack for enqueue operations.
        self.stack_out = []  # Stack for dequeue operations.

    def enqueue(self, x: int):
        """
        Add an element to the end of the queue.
        """
        self.stack_in.append(x)

    def dequeue(self) -> int:
        """
        Remove and return the front element of the queue.
        Transfers elements from stack_in to stack_out if necessary.
        """
        if not self.stack_out:
            # Transfer elements to stack_out to reverse order.
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        if not self.stack_out:
            raise IndexError("dequeue from an empty queue")

        return self.stack_out.pop()

# Example usage
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2