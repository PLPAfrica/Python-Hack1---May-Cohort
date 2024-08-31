# 1. Reverse a String Using a Stack

def reverse_string(s: str) -> str:
    stack = []
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    reversed_string = ''
    
    # Pop characters from the stack and add to the reversed_string
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage
print(reverse_string("hello"))  # Output: "olleh"



# 2. Implement a Queue Using Two Stacks

class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Push element onto stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack2:
            # Move elements from stack1 to stack2 if stack2 is empty
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


# 3. Find the Maximum Element in a List Using a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def find_max(self) -> int:
        if not self.head:
            return None
        
        max_value = self.head.data
        current_node = self.head
        while current_node:
            if current_node.data > max_value:
                max_value = current_node.data
            current_node = current_node.next
        
        return max_value

# Example usage
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4
