class Node:
    def __init__(self, value):
        # Initialize a node with a given value and no next node
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with no head node
        self.head = None
    
    def append(self, value):
        # Add a new node with the given value to the end of the list
        if not self.head:
            # If the list is empty, set the new node as the head
            self.head = Node(value)
        else:
            # Traverse to the end of the list
            current = self.head
            while current.next:
                current = current.next
            # Add the new node at the end
            current.next = Node(value)
    
    def find_max(self) -> int:
        # Check if the list is empty
        if not self.head:
            raise ValueError("List is empty")
        
        # Initialize max_value to the value of the head node
        max_value = self.head.value
        current = self.head
        
        # Traverse through the list to find the maximum value
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value
    
# Test data for LinkedList

# Initialize the linked list
linked_list = LinkedList()

# Append elements
linked_list.append(10)
linked_list.append(20)
linked_list.append(5)
linked_list.append(15)

# Find the maximum value
print(linked_list.find_max())  # Output should be 20

# Test with a list containing only one element
single_element_list = LinkedList()
single_element_list.append(7)
print(single_element_list.find_max())  # Output should be 7

# Test with an empty list (will raise a ValueError)
empty_list = LinkedList()
print(empty_list.find_max())
