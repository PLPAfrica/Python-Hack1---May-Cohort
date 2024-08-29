class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Add the element to stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, raise an exception (queue is empty)
        if not self.stack2:
            raise IndexError("Dequeue from an empty queue")
        
        # Return the element from stack2
        return self.stack2.pop()

# Testing the QueueWithStacks class
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  
    print(q.dequeue())  
