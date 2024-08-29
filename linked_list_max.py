class Node:
    def __init__(self, data):
        """Initialize a new node with data and a pointer to the next node."""
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
    
    def append(self, data):
        """Append a new node with the given data to the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def find_max(self) -> int:
        """Find and return the maximum element in the linked list."""
        if not self.head:
            raise ValueError("The linked list is empty")  # Handle empty list case
        
        max_value = self.head.data
        current_node = self.head
        while current_node:
            if current_node.data > max_value:
                max_value = current_node.data
            current_node = current_node.next
        
        return max_value

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print(ll.find_max())  # Output: 4
    
    # Test with a list with a single element
    single_ll = LinkedList()
    single_ll.append(10)
    print(single_ll.find_max())  # Output: 10
    
    # Test with an empty list (will raise ValueError)
    # empty_ll = LinkedList()
    # print(empty_ll.find_max())  # Uncommenting this will raise an error
