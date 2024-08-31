from collections import deque

class Node:
    """Represents a node in a linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    """A basic linked list implementation."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Appends a new node with the given data to the end of the list."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        """Prints the data of all nodes in the list."""
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete(self, value):
        """Removes the first occurrence of the given value from the list."""
        if self.head and self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current:
            if current.data == value:
                previous.next = current.next
                return
            previous = current
            current = current.next

class QueueWithStacks:
    """A queue implementation using two stacks."""
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def enqueue(self, item):
        """Adds an item to the end of the queue."""
        self.stack1.append(item)

    def dequeue(self):
        """Removes an item from the front of the queue."""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

def reverse_string(s):
    """Reverses the given string."""
    return s[::-1]

def reverse_linked_list(linked_list):
    """Reverses the given linked list."""
    previous = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    linked_list.head = previous

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.print_list()  # Output: 1 2
ll.delete(1)
ll.print_list()  # Output: 2

queue = QueueWithStacks()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

print(reverse_string("hello"))  # Output: olleh

ll = LinkedList()
ll.append(1)
ll.append(2)
reverse_linked_list(ll)
ll.print_list()  # Output: 2 1