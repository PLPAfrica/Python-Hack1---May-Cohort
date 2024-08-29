class QueueWithStacks:
    def __init__(self):
        """
        Initialize two stacks for the queue.
        stack1 is used for enqueue operations.
        stack2 is used for dequeue operations.
        """
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        """
        Add an element to the end of the queue.
        
        :param x: The element to be added to the queue.
        """
        self.stack1.append(x)

    def dequeue(self) -> int:
        """
        Remove and return the front element of the queue.
        
        :return: The front element of the queue.
        :raises IndexError: If the queue is empty.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        raise IndexError("dequeue from empty queue")

    def peek(self) -> int:
        """
        Return the front element of the queue without removing it.
        
        :return: The front element of the queue.
        :raises IndexError: If the queue is empty.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2[-1]
        raise IndexError("peek from empty queue")

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        
        :return: True if the queue is empty, False otherwise.
        """
        return not (self.stack1 or self.stack2)

    def get_size(self) -> int:
        """
        Get the number of elements in the queue.
        
        :return: The number of elements in the queue.
        """
        return len(self.stack1) + len(self.stack2)

# Example usage
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Front element (peek):", q.peek())  # Output: 1
    print("Queue size:", q.get_size())        # Output: 3
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2
    print("Queue empty:", q.is_empty())       # Output: False
    print(q.dequeue())  # Output: 3
    print("Queue empty:", q.is_empty())       # Output: True

    # Uncommenting the following line will raise an IndexError
    # print(q.dequeue())  # Raises IndexError: dequeue from empty queue
