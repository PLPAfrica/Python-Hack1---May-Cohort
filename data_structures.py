### 1. Reverse a string using stack 

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

def reverse_string(input_str):
    stack = Stack()
    for char in input_str:
        stack.push(char)

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

input_str = "Good Evening"
print(reverse_string(input_str))  

### 2. Implement a Queue Using Two stacks 


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
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, x: int):
        self.stack1.push(x)

    def dequeue(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        
        if self.stack2.is_empty():
            raise IndexError("Dequeue from an empty queue")
        
        return self.stack2.pop()



q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  
print(q.dequeue())  



### 3. Find the Maximum Element in a List Using a Linked List 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def find_max(self) -> int:
        if not self.head:
            return None
        max_value = self.head.data
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

# Example usage:
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  