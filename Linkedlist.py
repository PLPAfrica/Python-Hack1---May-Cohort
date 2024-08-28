class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the node
        self.next = None  # Pointer to the next node in the list

class LinkedList:
    def __init__(self):
        self.head = None  # Head of the list (initially empty)

    def append(self, data: int):
        # Create a new node with the provided data
        new_node = Node(data)
        
        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
        else:
            # Traverse to the end of the list and append the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        # If the list is empty, return an appropriate message or raise an error
        if self.head is None:
            raise ValueError("The list is empty.")
        
        # Initialize max_value with the head node's data
        max_value = self.head.data
        
        # Traverse the list to find the maximum value
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value
    
#    test with LinkedList
ll = LinkedList()
ll.append(10)
ll.append(5)
ll.append(15)
ll.append(7)
print(ll.find_max())  # Output: 15
