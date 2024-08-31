class QueueWithStacks:
    def __init__(self):
        # Stack to hold the incoming elements
        self.in_stack = []
        # Stack to hold the outgoing elements
        self.out_stack = []

    def enqueue(self, value: int) -> None:
        """Adds an element to the queue."""
        self.in_stack.append(value)

    def dequeue(self) -> int:
        """Removes and returns the front element of the queue."""
        if not self.out_stack:  # Check if out_stack is empty
            while self.in_stack:  # Transfer elements from in_stack to out_stack
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("dequeue from an empty queue")  # Handle empty queue case
        return self.out_stack.pop()  # Return the front element

# Example
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    print(q.dequeue())

"""
OUTPUT:
1
2

"""