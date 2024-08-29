# a) Define the Stack class:

# -  __init__: Initialize an empty list to store stack elements.
class Stack:
    def __init__(self):
        self.items = []

    # -  push: Add an element to the top of the stack.
    def push(self, item):
        self.items.append(item)

    # -  pop: Remove and return the top element of the stack.
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    # -  is_empty: Check if the stack is empty.
    def is_empty(self):
        return len(self.items) == 0

# b) Implement the reverse_string function:

# -  Initialize a Stack object.
def reverse_string(s: str) -> str:
    stack = Stack()
    for char in s:
        stack.push(char)

    # -  Push all characters of the input string onto the stack.
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()     # -  Pop all characters from the stack and append them to a result string.

    # -  Return the result string.
    return reversed_str

# Example usage
print(reverse_string("hello"))  # Output: "olleh"