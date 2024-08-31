class QueueWithStacks:
    """
    A queue implemented using two stacks.
    """
    def __init__(self):
        """
        Initialize two stacks to implement the queue.
        """
        self.s1 = []
        self.s2 = []

    def enqueue(self, x: int):
        """
        Add an element to the end of the queue.

        Args:
            x (int): The element to be added to the queue.
        """
        self.s1.append(x)

    def dequeue(self) -> int:
        """
        Remove and return the front element of the queue.

        If stack s2 is empty, transfer all elements from stack s1 to s2,
        which reverses their order, making the oldest element the top of s2.

        Returns:
            int: The front element of the queue.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        """
        Return the front element of the queue without removing it.

        Ensure that stack s2 has the elements for peeking at the front.

        Returns:
            int: The front element of the queue.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not self.s1 and not self.s2
