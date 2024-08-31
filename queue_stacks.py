# A queue can be implemented using two stacks.
# Let queue to be implemented be q and stacks used to implement q be stack1 and stack2.
# q can be implemented as follows: 

# By making enQueue operation costly): This method makes sure that oldest entered element is always at the top of stack 1, so that deQueue operation just pops from stack1. To put the element at top of stack1, stack2 is used.

# enQueue(q, x): 

# While stack1 is not empty, push everything from stack1 to stack2.
# Push x to stack1 (assuming size of stacks is unlimited).
# Push everything back to stack1.
# Here time complexity will be O(n)

# deQueue(q): 

# If stack1 is empty then error
# Pop an item from stack1 and return it
# Here time complexity will be O(1)

class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Push the element onto Stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If both stacks are empty, return None (or raise an exception)
        if not self.stack1 and not self.stack2:
            return None  # Or raise an exception like raise IndexError("Dequeue from empty queue")
        
        # If Stack2 is empty, move elements from Stack1 to Stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Pop the element from Stack2 (this will be the front of the queue)
        return self.stack2.pop()

# Example usage:
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2