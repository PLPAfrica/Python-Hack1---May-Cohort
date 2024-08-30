class QueueWithStacks:
    def __init__(self):
       
        self.stack1 = []  
        self.stack2 = []  

    def enqueue(self, x: int):
       
        self.stack1.append(x)  

    def dequeue(self) -> int:
        
        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Return the top element of stack2, which represents the front of the queue
        return self.stack2.pop() if self.stack2 else None

# Example usage
q = QueueWithStacks()
q.enqueue(1)  
q.enqueue(2)  

print(q.dequeue())  
print(q.dequeue())  
