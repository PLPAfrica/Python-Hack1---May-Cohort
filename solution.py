##1. Reverse String
def reverse_string(s: str) -> str:
    stack = []
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Pop characters from the stack to reverse the string
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example Usage:
print(reverse_string("hello"))  # Output: "olleh"

##2. Implement a Queue Using Two Stacks
class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Push element onto stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If stack2 is empty, move all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Pop the top element from stack2
        if self.stack2:
            return self.stack2.pop()
        else:
            return None  # Queue is empty

# Example Usage:
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2

##3. class Node
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
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def find_max(self) -> int:
        if not self.head:
            return None  # List is empty
        
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

