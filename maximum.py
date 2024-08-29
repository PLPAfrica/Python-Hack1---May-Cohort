class Node:
    def __init__(self, value: int):
        """
        Initialize a new node with a given value.
         
        Parameters:
        value (int): The value to be stored in the node.
        """
        self.value = value  # Store the value in the node
        self.next = None    # Initialize the next reference as None

class LinkedList:
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None  # The head of the list is initially None

    def append(self, value: int):
        """
        Append a new node with the given value to the end of the linked list.
        
        Parameters:
        value (int): The value to be added to the linked list.
        """
        new_node = Node(value)  # Create a new node with the provided value
        
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            # Traverse to the end of the list
            current = self.head
            while current.next:
                current = current.next
            # Append the new node at the end
            current.next = new_node

    def find_max(self) -> int:
        """
        Find and return the maximum value in the linked list.
        
        Returns:
        int: The maximum value in the linked list.
        
        If the list is empty, returns None.
        """
        if self.head is None:
            # If the list is empty, return None
            return None
        
        max_value = self.head.value  # Initialize max_value with the value of the head node
        current = self.head
        
        # Traverse the list to find the maximum value
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value

# Example usage
li = LinkedList()
li.append(32)  # Add value 32 to the list
li.append(76)   # Add value 76 to the list
li.append(12)  # Add value 12 to the list
li.append(8)  # Add value 8 to the list
li.append(354)   # Add value 354 to the list

# Find and print the maximum value in the linked list
print("The maximum element in the linked list is:", li.find_max())
