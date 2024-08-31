# Data Structures and Algorithms Challenges

# Question 1: Reverse a String Using a Stack
def reverse_string(s: str) -> str:
    stack = list(s)  # Directly convert the string into a list of characters
    return ''.join(stack[::-1])  # Efficiently reverse the list and join

# Examples for Question 1
print(reverse_string("hello"))      # Output: "olleh"
print(reverse_string("hackathon"))  # Output: "nohtakahc"
print(reverse_string("racecar"))    # Output: "racecar" (palindrome test)
print(reverse_string(""))           # Output: "" (empty string)

# Question 2: Implement a Queue Using Two Stacks
class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Dequeue from empty queue")
        return self.stack2.pop()

# Examples for Question 2
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  # Output: 10
q.enqueue(40)
print(q.dequeue())  # Output: 20
print(q.dequeue())  # Output: 30
print(q.dequeue())  # Output: 40
print(q.dequeue())  # Raises IndexError: Dequeue from empty queue

# Question 3: Find the Maximum Element in a List Using a Linked List
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
            raise ValueError("Cannot find max in an empty list")
        max_element = self.head.data
        current = self.head.next
        while current:
            max_element = max(max_element, current.data)
            current = current.next
        return max_element

# Examples for Question 3
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4

ll = LinkedList()
ll.append(-10)
ll.append(-20)
ll.append(-30)
ll.append(-5)
print(ll.find_max())  # Output: -5 (handles negative values)

ll_with_duplicates = LinkedList()
ll_with_duplicates.append(4)
ll_with_duplicates.append(4)
ll_with_duplicates.append(2)
print(ll_with_duplicates.find_max())  # Output: 4 (handles duplicates)

ll_single = LinkedList()
ll_single.append(42)
print(ll_single.find_max())  # Output: 42 (single element list)

empty_list = LinkedList()
print(empty_list.find_max())  # Raises ValueError: Cannot find max in an empty list

if __name__ == "__main__":
    # Main block examples to ensure functionality is correct
    pass
