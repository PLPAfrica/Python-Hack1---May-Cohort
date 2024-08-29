class QueueWithStacks:
    """
    A queue implemented using two stacks. This approach ensures that 
    elements are dequeued in the order they were enqueued (FIFO).
    """
    
    def __init__(self):
        """Initializes two stacks used to manage the queue."""
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        """Adds an element to the back of the queue.

        Args:
            x (int): The element to be added to the queue.
        """
        self.stack1.append(x)

    def dequeue(self) -> int:
        """Removes and return the front element of the queue.

        Returns:
            int: The front element of the queue.
            
        Raises:
            IndexError: If the queue is empty when attempting to dequeue.
        """
        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            raise IndexError("dequeue from empty queue")
        
        return self.stack2.pop()

    def is_empty(self) -> bool:
        """Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not (self.stack1 or self.stack2)

    def peek(self) -> int:
        """Get the front element of the queue without removing it.

        Returns:
            int: The front element of the queue.
            
        Raises:
            IndexError: If the queue is empty when attempting to peek.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            raise IndexError("peek from empty queue")
        
        return self.stack2[-1]

if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    
    try:
        print(q.dequeue())  # Expected output: 1
        print(q.dequeue())  # Expected output: 2
        print(q.dequeue())  # Expected to raise an IndexError
    except IndexError as e:
        print(f"Error: {e}")