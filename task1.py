#Task 1: Reverse a string using a stack
def reverse_string(s: str) -> str:
    stack = []  # Initialize an empty stack
    for character in s:
        stack.append(character)  # Push each character onto the stack

    reversed_string = ''
    while stack:
        reversed_string += stack.pop()  # Pop each character from the stack

    return reversed_string

input_string = "hello"
output_string = reverse_string(input_string)
print(output_string)  


#task 2: Implement a queue using two stacks
class QueueWithStacks:
    def __init__(self):
        self.stack1=[]  #stack to use for enqueue operation
        self.stack2=[]  #stack to se for dequeue operation

    def enqueue(self, x:int):
        self.stack1.append(x)

    def dequeue(self) ->int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop()) #move all elements from stack 1 to stack 2
        return self.stack2.pop()
    
q=QueueWithStacks()
q.enqueue(1)
q.enqueue(2)

print(q.dequeue())
print(q.dequeue())


print('\n\n')
#Task 3: Finding the maximum element in a list using a linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Store the reference to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list

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
            return float('-inf')  # Return negative infinity if the list is empty
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
print(ll.find_max())