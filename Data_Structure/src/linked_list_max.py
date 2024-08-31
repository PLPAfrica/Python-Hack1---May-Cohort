class Node:
    """Represents a node in the LinkedList."""
    
    def __init__(self, data):
        """
        Initialize a node with data and a reference to the next node.
        
        Args:
            data (int or float): The data to be stored in the node.
        """
        self.data = data
        self.next = None

class LinkedList:
    """LinkedList class to manage the linked list operations."""
    
    def __init__(self):
        """Initialize an empty LinkedList."""
        self.head = None

    def append(self, value):
        """
        Append a new node with the given value to the end of the list.

        Args:
            value (int or float): The value to be added to the list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self):
        """
        Find the maximum value in the linked list.

        Returns:
            int or float: The maximum value in the linked list.

        Raises:
            ValueError: If the list is empty.
        """
        if not self.head:
            raise ValueError("The linked list is empty.")
        
        max_value = self.head.data
        current = self.head.next
        
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value

    def print_list(self):
        """
        Print all the values in the linked list.

        Returns:
            list: A list of all values in the linked list.
        """
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.append(25)
    ll.append(65)

    # Print all items in the linked list
    print("LinkedList items:", ll.print_list())  # Output: LinkedList items: [3, 1, 4, 2]

    # Find and print the maximum value
    print("Maximum Value in LinkedList:", ll.find_max())  # Output: Maximum Value in LinkedList: 4
