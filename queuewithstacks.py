#Initialize two stacks
stack_in = []
stack_out = []

def enqueue(stack_in, x):
    #Add an element to the end of the queue
    stack_in.append(x)

def dequeue(stack_in, stack_out):
    #Removes the front element of the queue
    #If stack_out is empty, transfer all elements from stack_in to stack_out
    if not stack_out:
        while stack_in:
            stack_out.append(stack_in.pop())
    
    #If stack_out is still empty, then the queue is empty
    if not stack_out:
        raise IndexError("Dequeue from an empty queue")
    
    #Pop and return the element at the top of the stack_out, which is the front of the queue
    return stack_out.pop()

#test the functions
while True:
    try:
        #Ask user for input
        user_input = input("Enter a number to enqueue (or type 'done' to stop): ")
        
        #check is user wants to stop inputting numbers
        if user_input.lower() == 'done':
            break
        
        enqueue(stack_in, int(user_input))
    except ValueError:
        print("Please enter a valid number of 'done' to finish.") 
 
#Dequeue and print all elements       
print("\nDequeuing and printing all elements: ")
while True:
    try:
        #dequeue and print the next element
        print(dequeue(stack_in, stack_out))
    except IndexError:
        print("Queue is empty.")
        break