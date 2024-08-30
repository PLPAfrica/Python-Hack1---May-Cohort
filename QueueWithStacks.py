class QueueWithStacks:
    """A queue implemented using two stacks."""

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x: int) -> None:
        """
        Adds an element to the end of the queue.
        
        Args:
        x (int): The element to add to the queue.
        """
        self.stack_in.append(x)

    def dequeue(self) -> int:
        """
        Removes and returns the front element of the queue.
        
        Returns:
        int: The front element of the queue.
        
        Raises:
        IndexError: If the queue is empty.
        """
        if not self.stack_out:
            # Transfer elements from stack_in to stack_out if stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        if not self.stack_out:
            raise IndexError("dequeue from an empty queue")

        return self.stack_out.pop()