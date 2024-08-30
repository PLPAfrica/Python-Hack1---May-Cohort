class QueueWithStacks:
    def __init__(self):
        self.stack_newest_on_top = []
        self.stack_oldest_on_top = []

    def enqueue(self, value: int):
        self.stack_newest_on_top.append(value)

    def dequeue(self) -> int:
        if not self.stack_oldest_on_top:
            while self.stack_newest_on_top:
                self.stack_oldest_on_top.append(self.stack_newest_on_top.pop())
        
        return self.stack_oldest_on_top.pop()

q = QueueWithStacks()
q.enqueue(50)
q.enqueue(20)
q.enqueue(70)
print(q.dequeue())  # Output: 50
print(q.dequeue())  # Output: 20
print(q.dequeue())  #Output: 70
