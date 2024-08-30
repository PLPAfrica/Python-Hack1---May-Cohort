class Node:
    """
    A node in a singly linked list.
    """

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    A singly linked list.
    """

    def __init__(self):
        self.head = None

    def append(self, value: int):
        """
        Append a value to the end of the linked list.
        Args:
            value (int): The value to append.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find_max(self) -> int:
        """
        Find the maximum value in the linked list.
        Returns:
            int: The maximum value in the linked list.
        Raises:
            ValueError: If the linked list is empty.
        """
        if not self.head:
            raise ValueError("Linked list is empty")

        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print(f"Maximum value in the linked list: {ll.find_max()}")
