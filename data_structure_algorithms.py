### 1. Reverse a String Using a Stack
def reverse_string(s: str) -> str:
    stack = []
    
    for char in s:
        stack.append(char)
    
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

input_string = "hackathon"
output_string = reverse_string(input_string)
print(output_string)  


### 2. Implement a Queue Using Two Stacks
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
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  
print(q.dequeue())  
print(q.dequeue())  

### 3. Find the Maximum Element in a List Using a Linked List
class ListNode:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find_max(self) -> int:
        if not self.head:
            raise ValueError("The linked list is empty")
        
        max_value = self.head.data
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value


ll = MyLinkedList()
ll.append(7)
ll.append(2)
ll.append(9)
ll.append(5)
print(ll.find_max())  
