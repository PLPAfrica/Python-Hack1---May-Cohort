class Node:
    """Class to represent a node in a singly linked list."""
    def __init__(self, value):
        self.value = value 
        self.next_node = None  # Pointer to the next node

class LinkedList:
    """Class to represent a singly linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def append(self, value):
        """Append a new node with the given value to the end of the list."""
        new_node = Node(value) 
        if not self.head:
            self.head = new_node  # If the list is empty, set head to the new node
            return
        
        current_node = self.head  # Start from the head
        while current_node.next_node:  
            current_node = current_node.next_node
            
        current_node.next_node = new_node  # Link the new node at the end

    def find_max(self) -> int:
        """Return the maximum value in the linked list."""
        if not self.head:
            raise ValueError("The linked list is empty.")  # Handle empty list case

        max_value = self.head.value  # Initialize max_value with the head's value
        current_node = self.head.next_node  # Start from the second node
        
        while current_node:  # Traverse through the list
            if current_node.value > max_value:  # Update max_value if current node's value is greater
                max_value = current_node.value
            current_node = current_node.next_node  # Move to the next node
            
        return max_value

# Example
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print(ll.find_max())

"""
OUTPUT:
4
"""