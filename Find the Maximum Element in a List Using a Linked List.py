class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value: int):
        # Create a new node with the given value
        new_node = Node(value)
        
        # If the list is empty, set the new node as the head
        if not self.head:
            self.head = new_node
        else:
            # Traverse to the end of the list
            current = self.head
            while current.next:
                current = current.next
            # Append the new node
            current.next = new_node
    
    def find_max(self) -> int:
        if not self.head:
            raise ValueError("List is empty")
        
        # Initialize max_value with the value of the head node
        max_value = self.head.value
        current = self.head
        
        # Traverse the list to find the maximum value
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value
