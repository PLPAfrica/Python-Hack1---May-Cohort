## Appropriate approach to use is FIFO (First In, First Out) behavior, this will allow elements to be queued into stack1, and when dequeuing, elements are transferred to stack2 if stack2 is empty.
class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Push element to the first stack
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If second stack is empty, transfer elements from the first stack
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Pop and return the top element from the second stack
        return self.stack2.pop() if self.stack2 else None

# Example usage:
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
