class Node:
    """
    A Node class to represent each element in a singly linked list.
    
    Attributes:
        data (int): The data value stored in the node.
        next (Node): A reference to the next node in the linked list.
    """
    
    def __init__(self, data: int):
        """
        Initialize a new node with data and set the next node reference to None.

        Args:
            data (int): The data value for the node.
        """
        self.data = data  # Store data value
        self.next = None  # Initialize next as None


class LinkedList:
    """
    A LinkedList class to represent a singly linked list and perform operations on it.
    
    Attributes:
        head (Node): The head (first node) of the linked list.
    """
    
    def __init__(self):
        """
        Initialize an empty linked list with the head set to None.
        """
        self.head = None  # Start with an empty list
    
    def append(self, data: int):
        """
        Append a new node with the given data to the end of the linked list.

        Args:
            data (int): The data value to add to the list.
        
        Operation:
            - Create a new node with the specified data.
            - If the list is empty, set the new node as the head.
            - If the list is not empty, traverse to the end and append the new node.
        """
        new_node = Node(data)  # Create a new node with the given data
        
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            print(f"Appended {data} as the head of the list.")
        else:
            # If the list is not empty, traverse to the end of the list
            current = self.head
            while current.next is not None:
                current = current.next
            # Append the new node to the end of the list
            current.next = new_node
            print(f"Appended {data} to the list.")
    
    def find_max(self) -> int:
        """
        Find and return the maximum element in the linked list.

        Returns:
            int: The maximum data value in the list.
        
        Raises:
            ValueError: If the list is empty.
        
        Operation:
            - Traverse the list starting from the head.
            - Keep track of the maximum value encountered.
            - Return the maximum value after traversing the entire list.
        """
        if self.head is None:
            # Raise an error if the list is empty
            raise ValueError("The linked list is empty. Cannot determine the maximum value.")
        
        # Initialize max_value with the data of the head node
        max_value = self.head.data
        print(f"Starting find_max. Initial max value is {max_value}.")
        
        # Traverse the list and update max_value if a larger value is found
        current = self.head.next
        while current is not None:
            if current.data > max_value:
                print(f"Found a new max value {current.data} at node.")
                max_value = current.data
            current = current.next
        
        print(f"Maximum value in the list is {max_value}.")
        return max_value


# Example Usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print(ll.find_max())  # Output: 4
