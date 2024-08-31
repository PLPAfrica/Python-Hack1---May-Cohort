# Find the Maximum Element in a List Using a Linked List
class Node:
    def __init__(self, value: int):
        # A node is like a little box that holds a piece of data (value).
        # It also has a pointer (next) to the next node in the list.
        # Initially, this box doesn't point to any other box (next is None).
       
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        # Start with an empty linked list. No boxes (nodes) are in the list yet.
        self.head = None

    def append(self, value: int):
        # Create a new box (node) with the given value.
        new_node = Node(value)
        
        # If the list is empty, this new box will be the first box (head).
        if not self.head:
            self.head = new_node
            return
        
        # If there are already boxes in the list, find the last one.
        current = self.head
        while current.next:
            current = current.next
        
        # Attach the new box to the end of the list.
        current.next = new_node

    def find_max(self) -> int:
        # If the list is empty, there's no maximum value to find.
        if not self.head:
            raise ValueError("List is empty")

        # Start by assuming the first box's value is the maximum.
        max_value = self.head.value
        current = self.head
        
        # Look at each box in the list to find the highest value.
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value

# Example usage with big numbers to test the linked list.
ll = LinkedList()
ll.append(10)
ll.append(100)
ll.append(1000)
ll.append(1000000)
ll.append(100000000)
print(ll.find_max())  

## Output: 100000000
