
# 1. Reverse a String Using a Stack

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


def reverse_string(input_string):
  
    stack = Stack()

    for char in input_string:
        stack.push(char)

    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


input_str = "hello"
reversed_str = reverse_string(input_str)
print(f"Original string: {input_str}")
print(f"Reversed string: {reversed_str}")



# ===========================2. Implement a Queue Using Two Stacks===============================



class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []  
        self.stack_out = [] 

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.stack_in.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if not self.stack_out:
           
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        if not self.stack_out:
            raise IndexError("dequeue from an empty queue")

        return self.stack_out.pop()

    def is_empty(self):
        """Check if the queue is empty."""
        return not self.stack_in and not self.stack_out

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if not self.stack_out:
           
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        if not self.stack_out:
            raise IndexError("peek from an empty queue")

        return self.stack_out[-1]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.stack_in) + len(self.stack_out)


queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  
print(queue.peek())     
print(queue.size())     
print(queue.is_empty()) 

queue.dequeue()
queue.dequeue()

print(queue.is_empty()) 


 # ========================3. Find the Maximum Element in a List Using a Linked List=====================================
 

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Add a new node with the given value to the end of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self):
        """Find the maximum value in the linked list."""
        if self.head is None:
            raise ValueError("The linked list is empty")
        
        max_value = self.head.value
        current = self.head.next
        
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value

    def __str__(self):
        """Return a string representation of the linked list."""
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return " -> ".join(map(str, values))


linked_list = SinglyLinkedList()
linked_list.append(3)
linked_list.append(1)
linked_list.append(4)
linked_list.append(1)
linked_list.append(5)
linked_list.append(9)
linked_list.append(2)

print("Linked List:", linked_list)
print("Maximum value in the linked list:", linked_list.find_max())

