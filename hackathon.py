# 1. Reverse a string using a stack
def reverse_string(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
    reversed_string = ''.join(stack.pop() for _ in range(len(stack)))

    return reversed_string
print(reverse_string("hello"))

# 2. Implement a Queue Using Two Stacks
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

# 3. Find the maximum element in a list using a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self, data: int):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def find_max(self) -> int:
        if self.head is None:
            raise ValueError("List is empty")
    
        max_value = self.head.data
        current = self.head 

        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value
    
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())
