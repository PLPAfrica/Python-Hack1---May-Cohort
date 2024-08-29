# Stack implementation for reversing a string
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

def reverse_string(s: str) -> str:
    stack = Stack()
    
    # Push all characters onto the stack
    for char in s:
        stack.push(char)
    
    # Pop all characters from the stack and build the reversed string
    reversed_str = []
    while not stack.is_empty():
        reversed_str.append(stack.pop())
    
    return ''.join(reversed_str)


# Queue implementation using two stacks
class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, x: int):
        self.stack1.append(x)
    
    def dequeue(self) -> int:
        if not self.stack2:
            # Transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            raise IndexError("dequeue from empty queue")
        
        return self.stack2.pop()


# Linked List implementation to find the maximum element
class Node:
    def __init__(self, value: int = 0, next_node: 'Node' = None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value: int):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def find_max(self) -> int:
        if not self.head:
            raise ValueError("Empty list")
        
        max_value = self.head.value
        current = self.head.next
        
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value


# Example usage
if __name__ == "__main__":
    # Test reverse_string function
    print(reverse_string("hello"))  # Output: "olleh"

    # Test QueueWithStacks class
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2

    # Test LinkedList class
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print(ll.find_max())  # Output: 4
