class QueueWithStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueue operations
        self.stack2 = []  # Stack for dequeue operations

    def enqueue(self, x):
        #Adds an element to the queue.
        self.stack1.append(x)

    def dequeue(self):
        #Removes and returns the front element of the queue.
        if not self.stack2:
            # If stack2 is empty, transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if self.stack2:
            return self.stack2.pop()
        else:
            return None  # Queue is empty
    
    #Checks if the queue is empty.    
    def is_empty(self):
        
        return len(self.stack1) == 0 and len(self.stack2) == 0
        

def main():
    queue = QueueWithStacks()
    while True:
        element = input("Enter an element (or 'quit' to exit): ")
        if element.lower() == "quit":
            break
        queue.enqueue(int(element))

    # Now you can dequeue elements from the queue
    while not queue.is_empty():
        print(queue.dequeue())

if __name__ == "__main__":
    main()