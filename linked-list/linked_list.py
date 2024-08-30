class Node:
    def __init__(self, data):
        # Initialize the node with data and set the next node to None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize the linked list with a head node set to None
        self.head = None
    
    def append(self, data: int):
        # Create a new node with the given data
        new_node = Node(data)
        
        # If the linked list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return
        
        # Otherwise, find the last node and link it to the new node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def find_max(self) -> int:
        # Initialize max_value to the smallest possible number
        max_value = float('-inf')
        
        # Start at the head of the linked list
        current = self.head
        
        # Traverse the linked list to find the maximum value
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print(ll.find_max())  # Output: 4
