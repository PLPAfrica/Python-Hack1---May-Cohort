# Question 3
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int):
        """Append a new node with the given value to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        """Find the maximum value in the linked list."""
        if not self.head:
            raise ValueError("The linked list is empty")

        current = self.head
        max_value = current.value

        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value
