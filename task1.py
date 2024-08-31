class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    """
    Reverses a string using a stack data structure.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    stack = Stack()
    for char in s:
        stack.push(char)

    reversed_s = ""
    while not stack.is_empty():
        reversed_s += stack.pop()

    return reversed_s

# Example usage:
input_str = "Hello, World!"
print(reverse_string(input_str))  # Output: "!dlroW ,olleH"