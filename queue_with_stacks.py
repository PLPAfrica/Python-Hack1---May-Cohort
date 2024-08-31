#Implementing a Queue Using Two Stacks
class QueueWithStacks:
    def __init__(self):
        # We're using two stacks to build our queue.
        self.stack1 = []  # Stack1 will be used to add (enqueue) elements.
        self.stack2 = []  # Stack2 will be used to remove (dequeue) elements.

    def enqueue(self, x: int):
        # Let's add the element to the first stack.
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If the second stack is empty, we need to move all elements from the first stack to the second.
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If the second stack is still empty, it means our queue is empty.
        if not self.stack2:
            raise IndexError("Dequeue from an empty queue")

        # Now, we can remove and return the element from the top of the second stack.
        return self.stack2.pop()

# Example usage with simple numbers:
q = QueueWithStacks()
q.enqueue(400)
q.enqueue(20)
print(q.dequeue())  # Output: 400
print(q.dequeue())  # Output: 20
