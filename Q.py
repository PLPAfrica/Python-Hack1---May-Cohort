class QueueWithStacks:
    def __init__(self):
        self.stack1 = []  # Stack to handle enqueue operations
        self.stack2 = []  # Stack to handle dequeue operations

    def enqueue(self, x: int):
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            # If stack2 is still empty, the queue is empty
            raise IndexError("Dequeue from an empty queue")
        
        return self.stack2.pop()

# Example
queue = QueueWithStacks()
queue.enqueue(30)
queue.enqueue(43)

print(queue.dequeue())  # 1st output

queue.enqueue(83)

print(queue.dequeue())  #  2nd Output 
print(queue.dequeue())  # 3rd Output
