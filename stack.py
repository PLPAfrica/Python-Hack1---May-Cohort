class Stack:
    """A simple implementation of a stack data structure using a Python list."""
    
    def __init__(self):
        """Initializes an empty stack."""
        self.items = []

    def push(self, item):
        """Pushes an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Pops an item off the stack and return it.
        
        Returns:
            The item from the top of the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        """Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

def reverse(s: str) -> str:
    """Reverses a given string using a stack.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    stack = Stack()

    # Push all characters onto the stack
    for char in s:
        stack.push(char)

    # Pop all characters from the stack to reverse the string
    reversed_str = ''.join(stack.pop() for _ in range(len(s)))

    return reversed_str

if __name__ == "__main__":
    value = input("Enter string characters: ")
    try:
        print(reverse(value))
    except TypeError as e:
        print(f"Error: {e}")