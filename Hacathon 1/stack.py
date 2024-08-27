class QueueWithStacks:
    def __init__(self):
        # Initialize two stacks
        self.stack1 = []  # For enqueue operations
        self.stack2 = []  # For dequeue operations

    def enqueue(self, x: int):
        # Add element to stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If stack2 is empty, move elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, the queue is empty
        if not self.stack2:
            raise IndexError("Dequeue from an empty queue")
        
        # Remove and return the element from stack2
        return self.stack2.pop()


queue = QueueWithStacks()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
queue.enqueue(3)
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3
