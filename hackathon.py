# Reverse a string using a stack

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if self.items else None

def reverse_string(s: str) -> str:
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_str = ''
    while stack.items:
        reversed_str += stack.pop()
    
    return reversed_str

# Example Usage:
print(reverse_string("hello"))  # Output: "olleh"

# Implement a queue using two stacks

class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

# Example Usage:
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2

# Find the maximum element in a list using a linked list

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def find_max(self) -> int:
        if not self.head:
            return None
        
        max_val = self.head.data
        current = self.head
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val

# Example Usage:
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4
