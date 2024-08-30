class Stack:
    """
    A simple stack implementation using a list.
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Push an item onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Pop an item from the stack.
        Returns:
            The item at the top of the stack.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        """
        Check if the stack is empty.
        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    """
    Reverse the given string using a stack.
    Args:
        s (str): The string to reverse.
    Returns:
        str: The reversed string.
    """
    stack = Stack()

    # Push each character of the string onto the stack
    for char in s:
        stack.push(char)

    # Pop all characters from the stack to build the reversed string
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

# Example usage
if __name__ == "__main__":
    example_string = "hello"
    print(f"Original string: {example_string}")
    print(f"Reversed string: {reverse_string(example_string)}")


