class QueueWithStacks:
    def __init__(self):
        # Initialize two empty stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Add an element to the queue by pushing it onto stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If both stacks are empty, the queue is empty
        if not self.stack1 and not self.stack2:
            raise IndexError("Cannot dequeue from an empty queue")

        # If stack2 is empty, pop all elements from stack1 and push them onto stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # The front element of the queue is now at the top of stack2
        return self.stack2.pop()
    
queue = QueueWithStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.dequeue())  
print(queue.dequeue())  