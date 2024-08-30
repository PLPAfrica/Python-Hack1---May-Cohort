class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Pop an item off the stack."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    """Reverse the input string using a stack."""
    stack = Stack()  # Create an instance of Stack
    
    # Push all characters onto the stack
    for char in s:
        stack.push(char)
    
    # Pop all characters from the stack and construct the reversed string
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
        
    return reversed_str

# Example usage of reverse stringy
if __name__ == "__main__":
    print(reverse_string("hello")) 