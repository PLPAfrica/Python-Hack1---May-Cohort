#Task:Implement a queue using two stacks.

class QueueStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        if not isinstance(x, int):
            raise TypeError("Only integers can be enqueued")
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack1 and not self.stack2:
            raise IndexError("Dequeue from empty queue")
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            raise IndexError("Dequeue from empty queue")
        
        return self.stack2.pop()

