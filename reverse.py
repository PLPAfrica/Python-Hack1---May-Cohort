# a) Define the Stack class:

# -  __init__: Initialize an empty list to store stack elements.
# -  push: Add an element to the top of the stack.
# -  pop: Remove and return the top element of the stack.
# -  is_empty: Check if the stack is empty.


# b) Implement the reverse_string function:

# -  Initialize a Stack object.
# -  Push all characters of the input string onto the stack.
# -  Pop all characters from the stack and append them to a result string.
# -  Return the result string.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    stack = Stack()
    for char in s:
        stack.push(char)

    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

# Example usage
print(reverse_string("hello"))  # Output: "olleh"
