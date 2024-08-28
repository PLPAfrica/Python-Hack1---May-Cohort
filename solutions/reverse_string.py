class Stack:
    """
    A simple stack implementation using a list.
    """

    def __init__(self):
        self.items = []  # Initialize an empty list to act as the stack.

    def push(self, item):
        """
        Push an item onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Pop an item off the stack. Raises an error if the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    """
    Reverse a string using a stack.
    """
    stack = Stack()

    # Push all characters of the string onto the stack.
    for char in s:
        stack.push(char)

    reversed_string = []
    # Pop all characters from the stack to reverse the string.
    while not stack.is_empty():
        reversed_string.append(stack.pop())

    return ''.join(reversed_string)

# Example usage
print(reverse_string("hello"))  # Output: "olleh"