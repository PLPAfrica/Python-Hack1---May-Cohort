class QueueWithStacks:
    def __init__(self):
   # Main stack for enqueueing     
        self.stack1 = []  
    # Temporary stack for dequeuing    
        self.stack2 = []  

    def enqueue(self, x: int):
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack2:
            # If the temporary stack is empty, transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            # If both stacks are empty, the queue is empty
            raise IndexError("Queue is empty")

        return self.stack2.pop()
    
    