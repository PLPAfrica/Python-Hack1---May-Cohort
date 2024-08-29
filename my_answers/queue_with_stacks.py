class QueueWithStacks:
    def __init__(self):
    
        #Initialize two stacks to implement the queue.#
        self.stack1 = []  # Stack used for enqueue operations
        self.stack2 = []  # Stack used for dequeue operations
    
    def enqueue(self, x: int):
    
        #Add an element to the end of the queue.#
      
        self.stack1.append(x)  # Push the element onto stack1
    
    def dequeue(self) -> int:
        #Remove and return the element from the front of the queue.#
        if not self.stack2:
            # Transfer all elements from stack1 to stack2 to reverse their order
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is not empty, pop the front element
        if self.stack2:
            return self.stack2.pop()
        else:
            raise IndexError("Queue is empty")  # Queue is empty, cannot dequeue

# Example usage:
if __name__ == "__main__":
    # Create a queue using two stacks
    q = QueueWithStacks()

    # Enqueue operations (add tasks to the queue)
    q.enqueue(101)  
    q.enqueue(102)  
    q.enqueue(103)  
    q.enqueue(104)  
    q.enqueue(105)  

    # Dequeue operations (process tasks from the queue)
    print(q.dequeue())  
    print(q.dequeue())  
    print(q.dequeue())  
    print(q.dequeue())  
    print(q.dequeue()) 