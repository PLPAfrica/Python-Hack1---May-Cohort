#Implement a Queue Using Two Stacks
class QueueWithStacks:
    def __init__(self):
        # Two stacks: one for enqueue operations, one for dequeue operations
        self.stack1 = []#store elements to during enqueue
        self.stack2 = []#store elements to during dequeue
    
    def enqueue(self, x: int):
        # add element onto stack1
        self.stack1.append(x)
    
    def dequeue(self) -> int:
        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty after the transfer, the queue is empty
        if not self.stack2:
            raise IndexError("dequeue from an empty queue")
        
        # Pop the top element from stack2 (which is the front of the queue)
        return self.stack2.pop()


q = QueueWithStacks()
q.enqueue(1)# adds 1 to the queue
q.enqueue(2)# adds 2 to the queue
print(q.dequeue()) # removes and returns 1
print(q.dequeue()) # remove and returns 2
