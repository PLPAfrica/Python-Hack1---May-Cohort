class QueueWithStacks:
    # Initialize two stacks
    def __init__(self):   
        # Stack to handle enqueue operations    
        self.stack1 = []  
        # Stack to handle dequeue operations
        self.stack2 = []  

    """
    Add a call ID to the queue.
        
    Parameters:
    call_id (int): The ID of the call to be enqueued.
    """
    def enqueue(self, call_id: int):
        self.stack1.append(call_id)

    """
    Remove and return the call ID from the front of the queue.
        
    Returns:
    int: The ID of the call that is dequeued.

    Raises:
    IndexError: If there are no calls to process.
    """
    def dequeue(self) -> int:
        # Transfer elements from stack1 to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, the queue is empty
        if not self.stack2:
            raise IndexError("No calls to process")
        
        # Pop the call ID from stack2
        return self.stack2.pop()

# calls in a queue case
call_queue = QueueWithStacks()
# Enqueue call ID 1001
call_queue.enqueue(1001)  
# Enqueue call ID 1002
call_queue.enqueue(1002)  
# Output: 1001 (Call ID 1001 is dequeued first)
print(call_queue.dequeue()) 
# Output: 1002 (Call ID 1002 is dequeued next) 
print(call_queue.dequeue())  
