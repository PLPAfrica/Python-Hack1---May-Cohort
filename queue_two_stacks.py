class QueueWithStacks:
    def __init__(self):
        """Initialize two empty stacks for queue operations."""
        self.stack1 = []  # This stack is used for enqueue
        self.stack2 = []  # This stack is used for dequeue

    def enqueue(self, x: int):
        """Add an element to the queue."""
        self.stack1.append(x)  # Push the incoming element onto stack1

    def dequeue(self) -> int:
        """Remove and return the front element of the queue."""
        if not self.stack2:  # If stack2 is empty, we need to refill it
            while self.stack1:
                self.stack2.append(self.stack1.pop())  # Transfer elements to stack2
        if not self.stack2:  # If stack2 is still empty, the queue is empty
            raise IndexError("Dequeue from empty queue")
        return self.stack2.pop()  # Pop from stack2 to get the front element

# Example usage of queue with two stacks
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  
    print(q.dequeue())  