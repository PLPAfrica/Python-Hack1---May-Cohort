# Define a class for the queue that uses two stacks
class QueueWithStacks:
    def __init__(self):
        # Initialize two stacks
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x: int):
        # Push the element onto the input stack
        self.stack_in.append(x)

    def dequeue(self) -> int:
        # If the output stack is empty, move elements from input stack to output stack
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        # If the output stack is still empty, raise an error
        if not self.stack_out:
            raise IndexError("Dequeue from an empty queue")
        
        # Pop and return the top element from the output stack
        return self.stack_out.pop()

# Example usage
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  
    print(q.dequeue())  
