# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node in the linked list

# LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list as None
    
    # Method to append a new element to the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            current = self.head  # Start from the head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Set the new node as the next of the last node
    
    # Method to find the maximum element in the linked list
    def find_max(self) -> int:
        if not self.head:  # Check if the list is empty
            raise ValueError("The list is empty")
        
        max_value = self.head.data  # Initialize the max_value with the head node's data
        current = self.head.next  # Start from the second node
        
        while current:  # Traverse the linked list
            if current.data > max_value:  # Update max_value if current node's data is greater
                max_value = current.data
            current = current.next  # Move to the next node
        
        return max_value  # Return the maximum value found in the list


ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # It Outputs 4
