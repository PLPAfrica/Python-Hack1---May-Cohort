class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Push the element onto stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If stack2 is empty, we need to move elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                # Move elements from stack1 to stack2
                self.stack2.append(self.stack1.pop())
        # Now the oldest element is at the top of stack2
        # If stack2 is still empty, that means the queue was empty
        if self.stack2:
            return self.stack2.pop()
        else:
            raise IndexError("dequeue from empty queue")

# Test the QueueWithStacks implementation
q = QueueWithStacks()
q.enqueue(7)
q.enqueue(8)
print(q.dequeue())  
q.enqueue(9)
print(q.dequeue())  
print(q.dequeue())  
