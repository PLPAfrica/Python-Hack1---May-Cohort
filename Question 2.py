# Question 2
class QueueWithStacks:
    def __init__(self):
        self.stack1 = []  # Stack used for enqueue operations
        self.stack2 = []  # Stack used for dequeue operations

    def enqueue(self, x: int):
        # Push the element onto stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If stack2 is empty, transfer elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, the queue is empty and we cannot dequeue
        if not self.stack2:
            raise IndexError("dequeue from an empty queue")
        
        # Pop the top element from stack2
        return self.stack2.pop()
    

    