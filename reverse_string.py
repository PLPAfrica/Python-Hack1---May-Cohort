class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)
    
    def pop(self):
        """Pop an item from the stack. Returns None if the stack is empty."""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    """Reverse a string using a stack."""
    # Handle the edge case of an empty string
    if not s:
        return ""
    
    stack = Stack()
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.push(char)
    
    # Pop characters from the stack to form the reversed string
    reversed_str = ''.join(stack.pop() for _ in range(len(s)))
    
    return reversed_str

# Example usage:
if __name__ == "__main__":
    input_str = "hello"
    print(reverse_string(input_str))  # Output: "olleh"
    
    # Test with an empty string
    print(reverse_string(""))  # Output: ""
    
    # Test with a single character
    print(reverse_string("A"))  # Output: "A"
