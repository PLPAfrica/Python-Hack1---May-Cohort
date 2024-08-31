class QueueWithStacks:
    """A Queue implementation using two stacks."""
    
    def __init__(self):
        """Initialize two stacks to manage the queue operations."""
        self.stack1 = []  # Stack 1 for enqueue operations
        self.stack2 = []  # Stack 2 for dequeue operations
    
    def enqueue(self, x: int):
        """
        Add an element to the queue.

        Args:
            x (int): The element to add to the queue.
        """
        self.stack1.append(x)  # Push element onto stack1
        print(f"Enqueued {x}: Stack1 is now {self.stack1}")
    
    def dequeue(self) -> int:
        """
        Remove and return the front element of the queue.

        Returns:
            int: The front element of the queue.
        
        Raises:
            IndexError: If the queue is empty when trying to dequeue.
        """
        # If both stacks are empty, raise an error (queue is empty)
        if not self.stack1 and not self.stack2:
            raise IndexError("dequeue from an empty queue")
        
        # If stack2 is empty, move all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            print(f"Moved elements to Stack2: Stack2 is now {self.stack2}")

        # Pop the top element from stack2
        dequeued_element = self.stack2.pop()
        print(f"Dequeued {dequeued_element}: Stack2 is now {self.stack2}")
        return dequeued_element

# Example Usage
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2
