class QueueWithStacks:
    def __init__(self):
        # initialization of the two stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Adding the element to the stack
        self.stack1.append(x)

    def dequeue(self) -> int:
        # transferring all the elements from stack1 to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # If at all stack2 is empty after transferring, the queue is empty
        if not self.stack2:
            raise IndexError("dequeue from an empty queue")
        
        # pop and return the element from stack2
        return self.stack2.pop()
    

# An example in use
queue = QueueWithStacks()
queue.enqueue(9)
queue.enqueue(8)
print(queue.dequeue())
queue.enqueue(7)
print(queue.dequeue())
print(queue.dequeue())