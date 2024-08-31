class QueueWithStacks:
    def __init__(self):
        """
        This class implements a queue using two stacks. The enqueue operation is performed on stack1,
        and the dequeue operation is performed on stack2. When stack2 is empty, elements are transferred
        from stack1 to stack2 to ensure the correct order of elements.
        """
        # Initialize two stacks: stack1 for enqueue operations, stack2 for dequeue operations
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        """
        Adds an element to the back of the queue.

        Parameters:
        x (int): The element to be added to the queue.

        Returns:
        None: This method does not return any value. It modifies the queue by adding the given element.
        """
        # Push the element onto stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        """
        Removes and returns the front element of the queue.

        The dequeue operation is performed on stack2. If stack2 is empty, elements are transferred
        from stack1 to stack2 to ensure the correct order of elements.

        Raises:
        IndexError: If both stacks are empty, indicating that the queue is empty.

        Returns:
        int: The element at the front of the queue.
        """
        # If both stacks are empty, raise an IndexError
        if not self.stack1 and not self.stack2:
            raise IndexError("Dequeue from an empty queue")

        # If stack2 is empty, transfer elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Pop the element from stack2 (which is the front of the queue)
        return self.stack2.pop()

    def __str__(self):
        """
        Returns a string representation of the queue's current state.
        
        If stack2 is not empty, it represents the front of the queue in reverse order. 
        Otherwise, stack1 represents the back of the queue.
        
        Returns:
        str: A string representation of the queue.
        """
        if not self.stack2:
            return str(self.stack1)
        return str(self.stack2[::-1] + self.stack1)

# Example usage:
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue("Lesson1")
    q.enqueue("Lesson2")
    q.enqueue("Lesson3")
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2
