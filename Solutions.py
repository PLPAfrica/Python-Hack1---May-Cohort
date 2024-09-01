# Task 1: Reverse a string using a stack
def reverse_string(s: str) -> str:
    # Creating an empty list
    stack = []
    # Pushing each character of string to stack
    for char in s:
        stack.append(char)
    # Pop each character from stack and form a reversed string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    return reversed_string

print(reverse_string('hello'))

# Task 2: Implement a queue using two stacks.
class QueueWithStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # pushing new elements to stack 1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # if stack2 is empty, what's on stack1 must be moved to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # an error that must be returned when trying to dequeue an empty queue
        if not self.stack2:
            raise IndexError("dequeue from an empty queue")            

        return self.stack2.pop()

# test example:
q = QueueWithStack()  
q.enqueue(1)
q.enqueue(2) 
print(q.dequeue())
print(q.dequeue())


# Task 3: Find the Maximum Element in a List Using a Linked List
class Node:
    def __init__(self, data: int):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data: int):
        # Create a new node with the given data
        new_node = Node(data)
        
        # If the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
        else:
            # loop through the list to find the last node and append the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    # Creating a function that will go through the list and return the maximum value
    def find_max(self) -> int:
        # If the list is empty, raise an error
        if self.head is None:
            raise ValueError("List is empty")
        
        # Initialize max_value with the data of the head node
        max_value = self.head.data
        current = self.head
        
        # loop through the list and update max_value if a larger element is found
        while current is not None:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value

# Test Example:
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())

