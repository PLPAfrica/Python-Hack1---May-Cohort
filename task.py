#Reverse a String Using a Stack
def reverse_string(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string

result = reverse_string("hello")
print(result)  

# Implement a Queue Using Two Stacks

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

q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.dequeue())  


#Find the Maximum Element in a List Using a Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def find_max(self) -> int:
        max_value = float('-inf')
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  
