class QueueWithStacks:
    def __init__(self):
        # Initialize two stacks to implement the queue
        self.stack1 = []  # This will hold the integers to enqueue
        self.stack2 = []  # This will help with the dequeue operation
        
    def enqueue(self, item: int):
        # Add an integer to the end of the queue (push onto stack1)
        self.stack1.append(item)
        
    def dequeue(self) -> int:
        # Remove and return the front integer from the queue
        if not self.stack2:
            # If stack2 is empty, move all elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, the queue was empty to begin with
        if not self.stack2:
            raise IndexError("Dequeue from an empty queue")
        
        return self.stack2.pop()
    
    def is_empty(self) -> bool:
        # Return True if the queue is empty
        return not self.stack1 and not self.stack2
    
    def peek(self) -> int:
        # Return the front integer from the queue without removing it
        if not self.stack2:
            # If stack2 is empty, move all elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # If stack2 is still empty, the queue was empty to begin with
        if not self.stack2:
            raise IndexError("Peek from an empty queue")
        
        return self.stack2[-1]
    
queue = QueueWithStacks()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.is_empty())