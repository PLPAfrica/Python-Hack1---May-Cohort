class QueueWithStacks:
    def __init__(self):
        # Stack to handle enqueue operations
        self.stack_in = []
        # Stack to handle dequeue operations
        self.stack_out = []

    def enqueue(self, x: int) -> None:
        # Push element onto stack_in
        self.stack_in.append(x)

    def dequeue(self) -> int:
        # If stack_out is empty, transfer all elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        # Pop and return the top element from stack_out, which is the front of the queue
        if self.stack_out:
            return self.stack_out.pop()
        else:
            raise IndexError("dequeue from an empty queue")


# Example usage:
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2
