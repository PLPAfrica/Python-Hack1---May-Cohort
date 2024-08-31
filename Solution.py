# Stack implementation to reverse a string
class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item of the stack
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    # Create a stack instance
    stack = Stack()
    
    # Push each character of the string onto the stack
    for char in s:
        stack.push(char)
    
    # Pop all characters from the stack and build the reversed string
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str


# Queue implementation using two stacks
class QueueWithStacks:
    def __init__(self):
        # Initialize two empty stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Add an element to the queue (push onto stack1)
        self.stack1.append(x)

    def dequeue(self) -> int:
        # Remove and return the front element of the queue
        if not self.stack2:
            # Move elements from stack1 to stack2 to reverse their order
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Check if stack2 is empty (queue is empty)
        if not self.stack2:
            raise IndexError("Dequeue from an empty queue")
        
        # Pop the element from stack2 (front of the queue)
        return self.stack2.pop()


# Linked list implementation to find the maximum element
class Node:
    def __init__(self, value):
        # Initialize node with value and next pointer
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list
        self.head = None

    def append(self, value):
        # Add a new node with the given value to the end of the list
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        # Find and return the maximum value in the linked list
        if not self.head:
            raise ValueError("Linked list is empty")
        
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value
