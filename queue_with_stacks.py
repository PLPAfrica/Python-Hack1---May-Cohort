class QueueWithStacks:
    def _init_(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        self.stack1.push(x)

    def dequeue(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.pop()

# Example usage
if __name__ == "_main_":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2