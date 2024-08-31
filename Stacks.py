class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.items = []
    
    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)
    
    def pop(self):
        # Remove and return the item from the top of the stack
        # Raise an error if the stack is empty
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from an empty stack")
    
    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    # Create a stack to help reverse the string
    stack = Stack()
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.push(char)
    
    # Create a list to build the reversed string
    reversed_str = []
    
    # Pop all characters from the stack to form the reversed string
    while not stack.is_empty():
        reversed_str.append(stack.pop())
    
    # Convert the list of characters back into a string and return it
    print(''.join(reversed_str))

# Test cases for reverse_string function

# Test with a typical string
reverse_string("peter")  # Output should be "retep"

# Test with an empty string
reverse_string("")  # Output should be ""

# Test with a single character string
reverse_string("a")  # Output should be "a"

# Test with a string of spaces
reverse_string("hello world")  # Output should be "dlrow olleh"

# Test with a string containing numbers and symbols
reverse_string("123!@#")  # Output should be "#@!321"

# Test with a palindrome string
reverse_string("madam")  # Output should be "madam"

