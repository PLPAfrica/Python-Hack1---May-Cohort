# Define a Stack class to implement stack data structure
class Stack:
    # Initialize an empty list to hold stack elements
    def __init__(self):
        self.data = []
    
    # Add the item to the end of the list, simulating push operation
    def push(self, data):
        self.data.append(data)
    
    # Remove and return the last item from the list, simulating pop operation
    def pop(self):        
        if not self.is_empty():
            return self.data.pop()
        else:
            # Raise an exception if trying to pop from an empty stack
            raise IndexError("Pop from an empty stack")
    
    # Check if the stack is empty by verifying if the list length is zero
    def is_empty(self):        
        return len(self.data) == 0
    
    # Return the last item in the list without removing it
    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            # Raise an exception if trying to peek in an empty stack
            raise IndexError("Peek from an empty stack")

def reverse_string(s):
    # Create an instance of the Stack class
    stack = Stack()
    
    # Push each character onto the stack
    for char in s:        
        stack.push(char)
    
    # Initialize an empty string to build the reversed string
    reversed_str = ''
    
   # Pop characters from the stack and append them to the reversed string
    while not stack.is_empty():        
        reversed_str += stack.pop()
    
    # Return the reversed string
    return reversed_str

# Print the string
full_name = input("What is your name? ")
# Print the original string
print("Original String:", full_name)
# Print the reversed string using the reverse_string function
print("Reversed String:", reverse_string(full_name))
