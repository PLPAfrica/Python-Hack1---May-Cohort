class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Push element to stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If both stacks are empty, raise an error
        if not self.stack1 and not self.stack2:
            raise IndexError("Queue is empty")

        # If stack2 is empty, pop all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Pop the element from stack2 (this is the front element)
        return self.stack2.pop()

# Example usage:
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue()) 
print(q.dequeue())  
