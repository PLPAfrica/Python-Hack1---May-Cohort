# 1.  Reverse a string using stack

# Create an empty stack.

def createStack():
	stack = []
	return stack

# Function to determine the size of the stack


def size(stack):
	return len(stack)

# Stack is empty if the size is 0


def isEmpty(stack):
	if size(stack) == 0:
		return "true"

# Function to add an item to stack .
# It increases size by 1


def push(stack, item):
	stack.append(item)

# Function to remove an item from stack.
# It decreases size by 1


def pop(stack):
	if isEmpty(stack):
		return
	return stack.pop()

# A stack based function to reverse a string


def reverse(string):
	n = len(string)

	# Create a empty stack
	stack = createStack()

	# Push all characters of string to stack
	for i in range(0, n, 1):
		push(stack, string[i])

	# Making the string empty since all
	# characters are saved in stack
	string = ""

	# Pop all characters of string and
	# put them back to string
	for i in range(0, n, 1):
		string += pop(stack)

	return string


# Driver program to test above functions
string = "Hello"
string = reverse(string)
print("Reversed string is " + string)


# 2. Implement Queue using two stacks with costly enQueue() 
class QueueWithStacks:
    def __init__(self):
        # Initialize two stacks
        self.stack_in = []
        self.stack_out = []
    
    def enqueue(self, x: int):
        # Push the element onto stack_in
        self.stack_in.append(x)
    
    def dequeue(self) -> int:
        # If stack_out is empty, transfer elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        # If stack_out is still empty, the queue is empty
        if not self.stack_out:
            raise IndexError("dequeue from an empty queue")
        
        # Pop the top element from stack_out
        return self.stack_out.pop()

# Example usage
queue = QueueWithStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
queue.enqueue(4)
print(queue.dequeue())  # Output: 3
print(queue.dequeue())  # Output: 4

# 3. Find the Maximum Element in a List Using a Linked List
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data: int):
        # Create a new node
        new_node = Node(data)
        
        # If the linked list is empty, set the new node as the head
        if not self.head:
            self.head = new_node
            return
        
        # Traverse to the end of the list and append the new node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def find_max(self) -> int:
        if not self.head:
            raise ValueError("The linked list is empty.")
        
        # Initialize the maximum value with the head's data
        max_value = self.head.data
        current = self.head
        
        # Traverse the linked list to find the maximum value
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value

# Example usage
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(1)
linked_list.append(4)
linked_list.append(1)
linked_list.append(5)

print(linked_list.find_max())  # Output: 5
