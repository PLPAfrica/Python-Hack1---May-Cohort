class Node:
    """
    Represents a node in a singly linked list.
    """

    def __init__(self, data=None):  # Corrected method name
        self.data = data  # Node's data
        self.next = None  # Pointer to the next node

class LinkedList:
    """
    A singly linked list implementation.
    """

    def __init__(self):
        self.head = None  # Initialize the list with no head

    def append(self, data: int):
        """
        Append a new node with the given data to the end of the list.
        """
        new_node = Node(data)
        
        if not self.head:
            # If list is empty, set the new node as the head.
            self.head = new_node
        else:
            # Traverse to the end and append the new node.
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        """
        Find and return the maximum element in the linked list.
        Raises an error if the list is empty.
        """
        if not self.head:
            raise ValueError("find_max from an empty linked list")
        
        max_value = self.head.data  # Start with the head node's data.
        current = self.head.next
        
        # Traverse the list to find the maximum value.
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
# Example 2: Create an empty linked list and try to find the max
ll = LinkedList()
try:
    print(ll.find_max())
except ValueError as e:
    print(e)  # Output: find_max from an empty linked list

# Example 3: Create a linked list with duplicate elements
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
ll.append(4)
ll.append(3)
print(ll.find_max())  # Output: 4

# Example 4: Create a linked list with negative numbers
ll = LinkedList()
ll.append(-3)
ll.append(-1)
ll.append(-4)
ll.append(-2)
print(ll.find_max())  # Output: -1

# Example 5: Create a linked list with a large number of elements
import random
ll = LinkedList()
for _ in range(1000):
    ll.append(random.randint(1, 1000))
print(ll.find_max())  # Output: 1000 (or a random number between 1 and 1000)

# Example 6: Create a linked list with a mix of positive and negative numbers
ll = LinkedList()
ll.append(-5)
ll.append(10)
ll.append(-2)
ll.append(7)
ll.append(-10)
ll.append(3)
print(ll.find_max())  # Output: 10

# Example 7: Create a linked list and append elements in a loop
ll = LinkedList()
for i in range(10):
    ll.append(i)
print(ll.find_max())  # Output: 9

# Example 8: Create a linked list and append elements in a loop with a step
ll = LinkedList()
for i in range(0, 20, 2):
    ll.append(i)
print(ll.find_max())  # Output: 18

# Example 9: Create a linked list and append elements from a list
numbers = [3, 1, 4, 2, 5, 6]
ll = LinkedList()
for num in numbers:
    ll.append(num)
print(ll.find_max())  # Output: 6