class Stack:
    """A simple Stack class using a list to store elements."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def push(self, item: str):
        """Push an item onto the stack."""
        self.items.append(item)
    
    def pop(self) -> str:
        """Pop an item from the stack."""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()
    
    def peek(self) -> str:
        """Peek at the top item of the stack without removing it."""
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.items[-1]

def reverse_string(s: str) -> str:
    """
    Reverse a given string using a stack.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    stack = Stack()
    
    # Push all characters onto the stack
    for char in s:
        stack.push(char)
    
    # Pop all characters to get the reversed string
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

# Example Usage
if __name__ == "__main__":
    input_string = "hello"
    input_string1 = "come"
    print(f"Original string: {input_string}")
    print(f"Reversed string: {reverse_string(input_string)}")
    print(f"Original string: {input_string1}")
    print(f"Reversed string: {reverse_string(input_string1)}")
