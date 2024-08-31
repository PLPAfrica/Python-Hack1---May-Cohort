class Stack:
    """
    A stack implementation using a list. Follows Last-In-First-Out (LIFO) principle.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Add an item to the top of the stack.

        Args:
            item: The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the item from the top of the stack.

        Returns:
            The item from the top of the stack, or None if the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """
        Return the item from the top of the stack without removing it.

        Returns:
            The item from the top of the stack, or None if the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def get_all(self):
        """
        Get a list of all items in the stack.

        Returns:
            list: A list of all items in the stack from bottom to top.
        """
        return self.items

