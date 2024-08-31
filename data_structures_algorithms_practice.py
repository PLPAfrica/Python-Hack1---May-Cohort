def reverse_string(s: str) -> str:
    stack = []
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Pop characters from the stack to get the reversed string
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage
print(reverse_string("hello"))  # Output: "olleh"



class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, x: int):
        # Push element onto the first stack
        self.stack1.append(x)
    
    def dequeue(self) -> int:
        if not self.stack2:
            # Transfer all elements from stack1 to stack2, reversing the order
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Return the element from stack2
        return self.stack2.pop() if self.stack2 else None

# Example usage
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
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
    
    def find_max(self) -> int:
        if self.head is None:
            return None  # List is empty
        
        max_value = self.head.data
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value

# Example usage
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4
