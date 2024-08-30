#1. Reverse a String Using a Stack

def reverse_string(s: str) -> str:

    stack = []

    for char in s:
        stack.append(char)

    reversed_string = ""

    while stack:
        reversed_string += stack.pop()

    return reversed_string

print(reverse_string("Hello"))


#2. Implement a Queue Using Two Stacks
class QueueWithStacks:
    def __init__(self):
        self.input = []
        self.output = []

    def enqueue(self, x: int) -> None:
        self.input.append(x)

    def dequeue(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
            
        return self.output.pop()
    
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  
print(q.dequeue()) 


#3. Find the Maximum Element in a List Using a Linked List
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
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def find_max(self) -> int:
        if not self.head:
            return float('-inf')  # Or raise an exception if the list is empty
        
        max_element = self.head.data
        current = self.head

        while current:
            if current.data > max_element:
                max_element = current.data
            current = current.next
        
        return max_element
    
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max()) 