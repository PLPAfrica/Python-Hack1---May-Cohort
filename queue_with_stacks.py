class QueueWithStacks:
    """
    A queue implementation using two stacks.
    """

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        """
        Add an element to the end of the queue.
        Args:
            x (int): The element to add to the queue.
        """
        self.stack1.append(x)

    def dequeue(self) -> int:
        """
        Remove and return the front element of the queue.
        Returns:
            int: The front element of the queue.
        Raises:
            IndexError: If the queue is empty.
        """
        if not self.stack2:  # Transfer elements from stack1 to stack2 if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Dequeue from empty queue")
        return self.stack2.pop()

# Example usage
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(f"Dequeued element: {q.dequeue()}")  # Output: 1
    print(f"Dequeued element: {q.dequeue()}")  # Output: 2


