class Stack:
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Add an item to the top of the stack.
        
        :param item: The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the item from the top of the stack.
        
        :return: The item from the top of the stack.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Return the item from the top of the stack without removing it.
        
        :return: The item from the top of the stack.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        
        :return: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def get_size(self) -> int:
        """
        Get the number of items in the stack.
        
        :return: The number of items in the stack.
        """
        return len(self.items)

def reverse_string(s: str) -> str:
    """
    Reverse a given string using a stack.
    
    :param s: The string to be reversed.
    :return: The reversed string.
    """
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage
if __name__ == "__main__":
    test_string = "hello"
    print(f"Original string: {test_string}")  # Output: "hello"
    print(f"Reversed string: {reverse_string(test_string)}")  # Output: "olleh"
