class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Attempting to pop from an empty stack")
    
    def is_empty(self):
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = []
    while not stack.is_empty():
        reversed_string.append(stack.pop())
    
    return ''.join(reversed_string)

# Example usage
if __name__ == "__main__":
    print(reverse_string("hello"))  
    # Output: "olleh"
