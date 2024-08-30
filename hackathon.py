def reverse_string(s: str) -> str:
    # Initialize an empty stack
    stack = []
    
    # Push all characters of the string into the stack
    for char in s:
        stack.append(char)
    
    # Pop all characters from the stack and form the reversed string
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage
input_string = "hello"
output_string = reverse_string(input_string)
print(output_string)  



class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Push the element onto stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Pop the element from stack2
        if self.stack2:
            return self.stack2.pop()
        else:
            raise IndexError("dequeue from empty queue")

# Example usage
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue()) 
print(q.dequeue())  



class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        if not self.head:
            raise ValueError("The linked list is empty")
        
        max_value = self.head.data
        current = self.head.next
        
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






