# solution 1
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
    Reverses a string using a stack.

    Args:
        s (str): The input string.

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
print(reverse_string("hello"))  # Output: "olleh"

# solution 2
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

class QueueWithStacks:
    def __init__(self):
        self.inbound_stack = Stack()
        self.outbound_stack = Stack()

    def enqueue(self, x: int):
        """
        Adds an element to the queue.

        Args:
            x (int): The element to add.
        """
        self.inbound_stack.push(x)

    def dequeue(self) -> int:
        """
        Removes and returns the front element of the queue.

        Returns:
            int: The front element of the queue.
        """
        if self.outbound_stack.is_empty():
            while not self.inbound_stack.is_empty():
                self.outbound_stack.push(self.inbound_stack.pop())
        return self.outbound_stack.pop()

# Example usage:
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2

# solution 3
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Appends a new node with the given data to the end of the list.

        Args:
            data: The data to append.
        """
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def find_max(self) -> int:
        """
        Finds the maximum element in the list.

        Returns:
            int: The maximum element in the list.
        """
        if not self.head:
            return None
        max_element = self.head.data
        current = self.head
        while current:
            if current.data > max_element:
                max_element = current.data
            current = current.next
        return max_element

# Example usage:
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4