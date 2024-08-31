class Node:
    def __init__(self, data: int):
        self.data = data  # Store the value of the node
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Head of the linked list

    def append(self, data: int):
        
        # Create a new node
        new_node = Node(data)
        
        # If the linked list is empty, set the head to the new node
        if self.head is None:
            self.head = new_node
        else:
            
            # Traverse to the end of the linked list and append the new node
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        if self.head is None:
            raise ValueError("The list is empty.")
        
        # Initialize the maximum value with the head node's data
        max_value = self.head.data
        
        # Traverse through the linked list and find the maximum value
        current = self.head
        while current is not None:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value

ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)

print(ll.find_max())
