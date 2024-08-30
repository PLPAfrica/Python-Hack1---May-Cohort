# Define a class
class QueueWithStacks:
    def __init__(self):
        # create two stacks (lists) to manage the queue
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x: int):
        # Add the element to the end of stack_in
        self.stack_in.append(x)

    def dequeue(self) -> int:
        # If stack_out is empty, transfer all elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        # Return the top element from stack_out (FIFO order)
        return self.stack_out.pop()

# Example usage
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2
