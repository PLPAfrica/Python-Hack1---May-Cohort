class QueueWithStacks:
    def __init__(self):
        self.stack1 = []  # Input stack
        self.stack2 = []  # Output stack

    def enqueue(self, x: int):
        # Push the element onto stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack2:
            # Transfer elements from stack1 to stack2, reversing their order
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            # If stack2 is still empty, the queue is empty
            raise IndexError("dequeue from an empty queue")
        
        # Pop the top element from stack2
        return self.stack2.pop()

# Example usage
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2