# Question 1: Reverse a String Using a Stack

class Stack:
    """
    A simple stack implementation using a list.
    """
    def __init__(self):
        """Initializes an empty stack."""
        self.items = []

    def push(self, item):
        """Adds an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the top item from the stack.
        Returns None if the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    """Reverses a string using a stack."""
    stack = Stack()  # Create a stack instance
    for char in s:
        stack.push(char)  # Push each character onto the stack
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()  # Pop characters from the stack and build the reversed string
    return reversed_string

# Example usage
string = "hello"
reversed_string = reverse_string(string)
print(f"Original string: {string}")
print(f"Reversed string: {reversed_string}")


# Question 2: Implement a Queue Using Two Stacks

class QueueWithStacks:
    """
    A queue implementation using two stacks.
    """
    def __init__(self):
        """Initializes the queue with two empty stacks."""
        self.input_stack = Stack()
        self.output_stack = Stack()

    def enqueue(self, x: int):
        """Adds an element to the queue."""
        self.input_stack.push(x)  # Add the element to the input stack

    def dequeue(self) -> int:
        """Removes and returns the front element of the queue."""
        if self.output_stack.is_empty():  # If the output stack is empty
            while not self.input_stack.is_empty():  # Move elements from the input stack to the output stack
                self.output_stack.push(self.input_stack.pop())
        return self.output_stack.pop()  # Return the top element of the output stack

# Example usage
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2


# Question 3: Find the Maximum Element in a List Using a Linked List

class Node:
    """
    A node in a linked list.
    """
    def __init__(self, data):
        """Initializes a node with data."""
        self.data = data
        self.next = None

class LinkedList:
    """
    A singly linked list implementation.
    """
    def __init__(self):
        """Initializes an empty linked list."""
        self.head = None

    def append(self, data):
        """Appends a new node to the end of the linked list."""
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, the new node becomes the head
            return

        current = self.head
        while current.next is not None:
            current = current.next  # Traverse to the last node
        current.next = new_node  # Append the new node

    def find_max(self) -> int:
        """Finds the maximum element in the linked list."""
        if self.head is None:
            return None  # Return None if the list is empty
        max_value = self.head.data
        current = self.head.next
        while current is not None:  # Traverse the list
            if current.data > max_value:
                max_value = current.data  # Update max_value if a larger value is found
            current = current.next
        return max_value

# Example usage
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4