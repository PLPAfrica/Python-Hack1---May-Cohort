class ListElement:
    """
    An element in a singly linked list.
    """
    def __init__(self, value: int):
        """
        Initialize an element with the given value and next pointer.
        
        Args:
            value (int): The value of the element.
        """
        self.value = value
        self.next = None

class LinkedList:
    """
       Implementing a singly linked list and finding the maximum element in the list.
    """
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def append(self, value: int):
        """
        Append a new element to the end of the linked list.

        Args:
            value (int): The value to be added to the linked list.
        """
        new_element = ListElement(value)
        if self.head is None:
            self.head = new_element
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element

    def find_max(self) -> int:
        """
        Find the maximum element in the linked list.

        Returns:
            int: The maximum value in the linked list.
        """
        if self.head is None:
            raise ValueError("The linked list is empty.")
        
        max_value = self.head.value
        current = self.head.next
        
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value

    def empty(self) -> bool:
        """
        Check if the linked list is empty.

        Returns:
            bool: True if the linked list is empty, False otherwise.
        """
        return self.head is None
