# Step 1: Define the Node class
# The Node class will represent each element in the linked list.

class Node:
    def __init__(self, data):
        self.data = data  # The data the node holds
        self.next = None  # Pointer to the next node in the list
        
# Step 2: Define the LinkedList class
# The LinkedList class will manage the nodes and include methods to append data and find the maximum element.

class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty, so the head is None

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Add the new node at the end

    def find_max(self) -> int:
        if self.head is None:
            raise ValueError("The linked list is empty.")
        
        max_value = self.head.data  # Start with the head node's data as the maximum
        current = self.head.next  # Start checking from the second node
        
        while current:  # Traverse through the list
            if current.data > max_value:  # If the current node's data is greater, update max_value
                max_value = current.data
            current = current.next  # Move to the next node
        
        return max_value
    
# Step 3: Test the implementation
# Now let's test the LinkedList class and its find_max method.
    
# Create a linked list
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)

# Find and print the maximum value
print(ll.find_max())  # Output: 4

# Summary:

# Node Class: Each node has two attributes: data and next. 
# The data stores the value, and next points to the next node in the list.
# LinkedList Class: The linked list manages nodes. 
# The append method adds a node to the end of the list, and find_max traverses the list to find the maximum element.
# Find_max Method: This method starts with the first node's value as the initial maximum and then traverses the list,
# updating the maximum value whenever it finds a larger one. If the list is empty, it raises an exception.