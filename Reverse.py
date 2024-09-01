class Stack:
    def __init__(self):
        # Initializes an empty list
        self.items = []

    def push(self, item):
        # Adds an item
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    # Create a stack instance
    stack = Stack()

    for char in s:
        stack.push(char)

    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

print(reverse_string("hello"))