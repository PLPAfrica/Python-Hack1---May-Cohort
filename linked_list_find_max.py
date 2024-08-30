class Node:
    def __init__(self, data):
        # This initializes a node with given data and sets the next pointer to None
        # 'data' will hold the value of this node, and 'next' will point to the next node in the list
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        # This initializes an empty linked list with no head node yet
        self.head = None  

    def append(self, data):
        """
        Adds a new node with the given data to the end of the linked list.
        """
        # Create a new node with the provided data
        new_node = Node(data)  
        
        # Check if the list is empty
        if self.head is None:  
            # If the list is empty, the new node becomes the head of the list
            self.head = new_node
        else:
            # If the list is not empty, find the last node to attach the new node to
            current = self.head  # Start from the head node
            
            # Traverse the list until we reach the last node
            while current.next:  
                current = current.next  # Move to the next node
            
            # Attach the new node to the end of the list
            current.next = new_node  

    def find_max(self):
        """
        Finds and returns the maximum element in the linked list.
        If the list is empty, returns None.
        """
        # Check if the list is empty
        if self.head is None:  
            return None  # Return None if the list is empty
        
        # Initialize max_value with the first node's data
        max_value = self.head.data  
        
        # Traverse the list starting from the second node
        current = self.head.next  # Start with the second node
        
        while current:  # Continue until we reach the end of the list (current becomes None)
            # Compare each node's data with the current max_value
            if current.data > max_value:  
                # If a node's data is greater than max_value, update max_value
                max_value = current.data  
            
            # Move to the next node
            current = current.next  
        
        # Return the maximum value found
        return max_value  

# usage
ll = LinkedList()  # Create an empty linked list
ll.append(3) 
ll.append(1) 
ll.append(4) 
ll.append(2)  
ll.append(6)
print(ll.find_max())  # Gives 6
