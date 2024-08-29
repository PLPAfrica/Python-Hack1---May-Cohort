class QueueWithStacks:
    def __init__(self):
        self.stack1 = []  # Stack to hold incoming elements
        self.stack2 = []  # Stack to hold elements for dequeue operation
    
    def enqueue(self, x: int):
        """Add an element to the queue."""
        self.stack1.append(x)
    
    def dequeue(self) -> int:
        """Remove and return the front element of the queue."""
        if not self.stack1 and not self.stack2:
            raise IndexError("Dequeue from empty queue")  # Handle empty queue case
        
        # If stack2 is empty, transfer elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()

# Example usage:
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    
    q.enqueue(3)
    print(q.dequeue())  # Output: 2
    
    print(q.dequeue())  # Output: 3
    
    # Uncommenting the following line will raise an IndexError because the queue is empty
    # print(q.dequeue())  
