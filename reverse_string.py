class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def reverse_string(s: str) -> str:
    """
    Reverse a string using a stack.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        ValueError: If the input is not a string.

    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(n), where n is the length of the input string.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    stack = Stack()

    # Push all characters onto the stack
    for char in s:
        stack.push(char)

    reversed_string = []

    # Pop characters from the stack to build the reversed string
    while not stack.is_empty():
        reversed_string.append(stack.pop())

    return ''.join(reversed_string)
