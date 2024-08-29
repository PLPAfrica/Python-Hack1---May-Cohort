#1.
def reverse_string(s: str) -> str:

    stack = []  # Create a stack to store characters

    
    for alph in s:
        stack.append(alph) # Adding each character onto the stack

    
    totAlph = ""
    while stack:
        totAlph += stack.pop() # Pop each letter from  the stack and append to totAlph

    
    return totAlph

print(reverse_string("karabo")) # call and print reverse_string function returned string





#2.
class QueueWithStacks: #Implimenting class
    def __init__(self):
        self.stack1 = []  # Inbound stack
        self.stack2 = []  # Outbound stack

    def enqueue(self, x: int) -> None: 
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack2:  # If stack2 stack is empty
            while self.stack1:  # Move all elements from stack1 to stack2
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

queue =  QueueWithStacks() #Creating class object

#Calling method using class objects 
queue.enqueue(1) 
queue.enqueue(2)

print(queue.dequeue())
print(queue.dequeue())



#3.

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

    def find_max(self):
        if not self.head:
            return None
        max_element = self.head.data
        current_node = self.head.next
        while current_node:
            if current_node.data > max_element:
                max_element = current_node.data
            current_node = current_node.next
        return max_element


ll = LinkedList() #Linked list Object

#Appending the linked list
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max()) #Call find_max method and print max value