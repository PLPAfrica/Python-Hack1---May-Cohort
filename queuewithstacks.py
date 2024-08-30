class QueueWithStacks:
    def __init__(self):
    #Initialize two stacks
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x:int):
        #Add an element to the end of the queue
        self.stack_in.append(x)

    def dequeue(self)-> int:
        #Removes the front element of the queue
        #If stack_out is empty, transfer all elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        #If stack_out is still empty, then the queue is empty
        if not self.stack_out:
            raise IndexError("Dequeue from an empty queue")
        
        #Pop and return the element at the top of the stack_out, which is the front of the queue
        return self.stack_out.pop()

#test the functions
if __name__ == '__main__':
    q = QueueWithStacks()
    while True:
        try:
            #Ask user for input
            user_input = input("Enter a number to enqueue (or type 'done' to stop): ")
            
            #check is user wants to stop inputting numbers
            if user_input.lower() == 'done':
                break
            
            q.enqueue(int(user_input))
        except ValueError:
            print("Please enter a valid number of 'done' to finish.") 
    
    #Dequeue and print all elements       
    print("\nDequeuing and printing all elements: ")
    while True:
        try:
            #dequeue and print the next element
            print(q.dequeue())
        except IndexError:
            print("Queue is empty.")
            break