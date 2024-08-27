class Node:
    """A Node in a singly linked list."""

    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list."""

    def __init__(self):
        self.head = None

    def append(self, data: int) -> None:
        """Appends a new node with the given data to the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        """Finds the maximum element in the linked list."""
        if not self.head:
            raise ValueError("The linked list is empty")

        # Initialize the max value with the head node's data
        max_value = self.head.data
        current = self.head

        # Traverse the list to find the max value
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value


# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print(ll.find_max())  # Output: 4
