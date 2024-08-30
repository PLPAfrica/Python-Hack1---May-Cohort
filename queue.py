class QueueWithStacks:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, x: int):
        self.stack_enqueue.append(x)

    def dequeue(self) -> int:
        if not self.stack_dequeue:
            if not self.stack_enqueue:
                raise IndexError("Queue is empty")
            
            # Transfer all elements from stack_enqueue to stack_dequeue
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        
        return self.stack_dequeue.pop()

# Example usage
q = QueueWithStacks()
q.enqueue(6)
q.enqueue(8)
print(q.dequeue())  
print(q.dequeue())