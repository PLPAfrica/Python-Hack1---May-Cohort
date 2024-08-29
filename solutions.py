### 1. Reverse a String Using a Stack
def reverse_string(s: str) -> str:
    # Initialize an empty stack (list in this case)
    stack = []
    
    # Push each character of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Initialize an empty string to hold the reversed string
    reversed_str = ""
    
    # Pop each character from the stack and add it to the reversed string
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage:
input_string = "hello"
output_string = reverse_string(input_string)
print(output_string)  # Output: "olleh"

### 2. Implement a Queue Using Two Stacks
class QueueWithStacks:
    def __init__(self):
        # Two stacks to simulate the queue behavior
        self.stack_in = []  # Stack to handle incoming elements
        self.stack_out = []  # Stack to handle outgoing elements

    def enqueue(self, x: int):
        # Push element onto the stack_in
        self.stack_in.append(x)

    def dequeue(self) -> int:
        # If stack_out is empty, move elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        # Pop the top element from stack_out, which is the front of the queue
        return self.stack_out.pop() if self.stack_out else None
    
### 3. Find the Maximum Element in a List Using a Linked List
class Node:
    def __init__(self, data):
        # Initialize a node with data and next pointer
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize the linked list with a head pointer
        self.head = None

    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        
        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
        
        # Otherwise, traverse to the end of the list and append the new node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def find_max(self) -> int:
        # If the list is empty, raise an error
        if not self.head:
            raise ValueError("The list is empty")
        
        # Initialize max_value with the first node's data
        max_value = self.head.data
        
        # Traverse the list to find the maximum value
        current_node = self.head
        while current_node:
            if current_node.data > max_value:
                max_value = current_node.data
            current_node = current_node.next
        
        return max_value

    