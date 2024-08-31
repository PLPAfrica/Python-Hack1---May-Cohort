class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    stack = Stack()
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.push(char)
    
    # Pop all characters from the stack and form the reversed string
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

# Test
print(reverse_string("hello"))  # Output: "olleh"


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
        return self.stack2.pop()

# Test
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
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
            return float('-inf')  # Return negative infinity if the list is empty
        
        max_value = self.head.data
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

# Test
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4
