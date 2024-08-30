class QueueWithStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x: int):
        self.stack_in.append(x)

    def dequeue(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    
        if not self.stack_out:
            raise IndexError("dequeue from an empty queue")
        return self.stack_out.pop()

# Example
if __name__ == "__main__":
    queue = QueueWithStacks()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.dequeue())  # Output: 10
    queue.enqueue(40)
    print(queue.dequeue())  # Output: 20
    print(queue.dequeue())  # Output: 30
    print(queue.dequeue())  # Output: 40
