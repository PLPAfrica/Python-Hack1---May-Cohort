class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from an empty stack")
    
    def is_empty(self):
        return len(self.stack) == 0

def reverse_string(s: str) -> str:
    stack = Stack()
    
    # Push all characters onto the stack
    for char in s:
        stack.push(char)
    
    # Pop all characters from the stack and build the reversed string
    reversed_str = []
    while not stack.is_empty():
        reversed_str.append(stack.pop())
    
    return ''.join(reversed_str)

# Example usage
print(reverse_string("hello"))  # Output: "olleh"
