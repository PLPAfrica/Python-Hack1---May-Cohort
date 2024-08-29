class QueueWithStacks:
    def __init__(self):
        """
        Initialize the queue using two stacks.
        
        stack1: Used for enqueue operations.
        stack2: Used for dequeue operations.
        """
        self.stack1 = []  # Stack used for adding elements to the queue
        self.stack2 = []  # Stack used for removing elements from the queue

    def enqueue(self, x: int):
        """
        Add an element to the end of the queue.
        
        Parameters:
        x (int): The element to be added to the queue.
        """
        self.stack1.append(x)  # Push the new element onto stack1

    def dequeue(self) -> int:
        """
        Remove and return the front element of the queue.
        
        Returns:
        int: The front element of the queue, or None if the queue is empty.
        """
        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Return the top element of stack2, which represents the front of the queue
        return self.stack2.pop() if self.stack2 else None

# Example usage
q = QueueWithStacks()
q.enqueue(1)  # Add value 1 to the queue
q.enqueue(2)  # Add value 2 to the queue

print(q.dequeue())  # Remove and print the front element of the queue (should print 8)
print(q.dequeue())  # Remove and print the next front element of the queue (should print 4)
