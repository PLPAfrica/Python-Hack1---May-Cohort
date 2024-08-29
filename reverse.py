class Stack:
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []  # List to hold stack elements

    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Parameters:
        item: The item to be added to the stack.
        """
        self.items.append(item)  # Append the item to the end of the list

    def pop(self):
        """
        Remove and return the item from the top of the stack.
        
        Returns:
        The item removed from the top of the stack.
        """
        return self.items.pop()  # Remove and return the last item from the list

    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
        bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0  # Return True if the stack has no elements

def reverse(s: str) -> str:
    """
    Reverse a given string using a stack.
    
    Parameters:
    s (str): The string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    stack = Stack()  # Create a new stack
    # Push each character of the string onto the stack
    for char in s:
        stack.push(char)

    reversed_str = ''  # Initialize an empty string to build the reversed string
    # Pop each character from the stack and append to the reversed string
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str  # Return the reversed string

# Example usage
value = input("Enter any string of your choice:")  # Prompt user for input
print(reverse(value))  # Print the reversed string
