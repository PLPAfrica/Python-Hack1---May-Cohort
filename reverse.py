class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        return self.stack.pop()

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0


def reverse_string(s: str) -> str:
    """Reverse the input string using a stack."""
    stack = Stack()  # Create an instance of the Stack class
    for char in s:
        stack.push(char)  # Push each character of the string onto the stack

    reversed_string = ""  # Initialize an empty string to store the reversed result
    while not stack.is_empty():
        reversed_string += stack.pop()  # Pop characters from the stack and append to the result

    return reversed_string


# User prompt to get input from the user
input_string = input("Enter a string: ") 
output_string = reverse_string(input_string)
print(f"The reversed string is: {output_string}")

"""
OUTPUT:
Enter a string: hello
The reversed string is: olleh
"""