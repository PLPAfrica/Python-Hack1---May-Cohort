#Reverse a String Using a Stack
def reverse_string(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

#Eg insert your country
input_string = input("Enter a word of your choice:")
reversed_string = reverse_string(input_string)
print(f"Original String: {input_string}")
print(f"Reversed String: {reversed_string}")

#Queue Using Two Stacks
class QueueWithStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x: int):
        self.stack_in.append(x)

    def dequeue(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop() if self.stack_out else None

#Output:
output = QueueWithStacks()
output.enqueue(1)
output.enqueue(2)
print(output.dequeue())  # Output: 1
print(output.dequeue())  # Output: 2


#Find the Maximum Element in a List Using a Linked List
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find_max(self) -> int:
        if not self.head:
            return None  # Or raise an exception if preferred
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

#Output
link = LinkedList()
link.append(6)
link.append(1)
link.append(8)
link.append(9)
print(link.find_max()) 