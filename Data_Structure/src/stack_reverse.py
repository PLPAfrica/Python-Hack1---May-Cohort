class Stack:
    
    """
    A class representing a stack data structure.

    Attributes:
    stack (list): A list to store the elements of the stack.

    Methods:
    push(item): Adds an item to the top of the stack.
    pop(): Removes and returns the top item from the stack.
    is_empty(): Checks if the stack is empty.
    """
    def __init__(self):
        """
        Initializes an empty list to represent the stack.
        """
        self.stack = []

    def push(self, item):
        """
        Adds an item to the top of the stack.

        Parameters:
        item (any): The item to be added to the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Removes and returns the top item from the stack.

        Returns:
        any: The top item from the stack, or None if the stack is empty.
        """
        return self.stack.pop() if not self.is_empty() else None

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
        bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0


def reverse_string(s: str) -> str:
    """
    Reverses a given string using a stack.

    Parameters:
    s (str): The input string to be reversed.

    Returns:
    str: The reversed string.

    Raises:
    ValueError: If the input is not a string.
    """
    # Check if the input is a string, raise an error if not
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    # Initialize a stack object to store characters
    stack = Stack()

    # Iterate over each character in the string
    for char in s:
        # Push each character onto the stack
        stack.push(char)

    # Initialize an empty string to store the reversed string
    reversed_str = ""

    # While the stack is not empty
    while not stack.is_empty():
        # Pop characters from the stack and append to the reversed string
        reversed_str += stack.pop()

    # Return the reversed string
    return reversed_str


print(reverse_string("Wellcome To My Data Structure Class Let's Have Fun Together!"))
