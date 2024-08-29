class QueueWithStacks:
    def __init__(self):
        # Initialize two stacks
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x: int):
        # Push element onto stack_in
        self.stack_in.append(x)

    def dequeue(self) -> int:
        # If stack_out is empty, move all elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        # If stack_out is still empty, the queue is empty (should raise an error)
        if not self.stack_out:
            raise IndexError("dequeue from an empty queue")
        
        # Pop and return the top element from stack_out
        return self.stack_out.pop()

# Example usage
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  
    print(q.dequeue())  
