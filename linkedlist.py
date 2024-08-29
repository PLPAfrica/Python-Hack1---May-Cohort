class Node:
    """
    A Node in a singly linked list.

    Attributes:
        value (int): The value stored in the node.
        next (Node): A reference to the next node in the list.
    """
    
    def __init__(self, value: int):
        """Initializes a node with a given value and set the next node to None."""
        self.value = value
        self.next = None

class LinkedList:
    """
    A singly linked list implementation.

    Attributes:
        head (Node): The first node in the linked list.
    """
    
    def __init__(self):
        """Initialize an empty linked list with no head node."""
        self.head = None

    def append(self, value: int):
        """Append a new node with the given value to the end of the linked list.

        Args:
            value (int): The value to append to the list.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        """Finds and returns the maximum value in the linked list.

        Returns:
            int: The maximum value in the list.

        Raises:
            ValueError: If the list is empty.
        """
        if self.head is None:
            raise ValueError("Cannot find maximum in an empty linked list")

        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next

        return max_value

    def is_empty(self) -> bool:
        """Checks if the linked list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.head is None

if __name__ == "__main__":
    li = LinkedList()

    # Collect integers from the user
    while True:
        try:
            value = input("Enter an integer to append to the linked list (or type 'done' to finish): ")
            if value.lower() == 'done':
                break
            li.append(int(value))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Find and print the maximum element in the linked list
    try:
        print("The maximum element in the linked list is:", li.find_max())
    except ValueError as e:
        print(f"Error: {e}")