# class to hold all functions
class QueueWithStacks:
    def __init__(self):
        # Initialize two stacks to simulate the queue
        self.stack1 = []  # Stack used for enqueue operations
        self.stack2 = []  # Stack used for dequeue operations

    def enqueue(self, x: int):
        """
        Adds an element to the end of the queue.
        """
        # Push new element onto stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        """
        This helps remove and return the front element of the queue.
        If the queue is empty, returns -1.
        """
        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())  # Pop from stack1 and push onto stack2

        # If stack2 is still empty, return -1 indicating the queue is empty
        if not self.stack2:
            return -1
        
        # Pop and return the top element from stack2, which is the front of the queue
        dequeued_element = self.stack2.pop()
        return dequeued_element


# Example usage
q = QueueWithStacks()     # create a queue stack variable
q.enqueue(1)  # Enqueue 1
q.enqueue(2)  # Enqueue 2
q.enqueue(3)  # Enqueue 3
print(q.dequeue()) 
print(q.dequeue())  
print(q.dequeue())