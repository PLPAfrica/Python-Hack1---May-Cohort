class QueueWithStacks:
    def __init__(self):
        # Initialize two empty stacks: stack1 and stack2
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, x: int):
        # Add an element to stack1 (the input stack)
        self.stack1.append(x)
    
    def dequeue(self) -> int:
        # Check if stack2 is empty
        if not self.stack2:
            # If stack2 is empty, transfer all elements from stack1 to stack2
            # This reverses the order of elements
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, raise an error (queue is empty)
        if self.stack2:
            return self.stack2.pop()
        raise IndexError("Dequeue from an empty queue")
    
# Test data for QueueWithStacks

# Initialize the queue
queue = QueueWithStacks()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue elements
print(queue.dequeue())  # Output should be 1
print(queue.dequeue())  # Output should be 2

# Enqueue more elements
queue.enqueue(4)
queue.enqueue(5)

# Dequeue elements
print(queue.dequeue())  # Output should be 3
print(queue.dequeue())  # Output should be 4
print(queue.dequeue())  # Output should be 5

# Attempt to dequeue from an empty queue (will raise an IndexError)
print(queue.dequeue())
