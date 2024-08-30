class QueueWithStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x: int):
        self.stack_in.append(x)

    def dequeue(self) -> int:
        # Transfer elements from stack_in to stack_out if stack_out is empty
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        # Check if stack_out has elements to pop
        if self.stack_out:
            return self.stack_out.pop()
        else:
            raise IndexError("Dequeue from an empty queue")

# Example usage
queue = QueueWithStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  
print(queue.dequeue()) 

queue.enqueue(4)
print(queue.dequeue())  
print(queue.dequeue())  