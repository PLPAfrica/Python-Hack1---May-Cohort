class Node:
    """
    A node in the singly linked list.
    """
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    """
    A singly linked list.
    """
    def __init__(self):
        self.head = None

    def append(self, data: int) -> None:
        """
        Append a new node with the given data to the end of the list.
        
        Args:
        data (int): The data to append to the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

    def find_max(self) -> int:
        """
        Find the maximum element in the linked list.
        
        Returns:
        int: The maximum element in the list.
        
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