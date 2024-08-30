class Node:
    def __init__(self, data):
        """Initialize a new node."""
        self.data = data  # Node data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None  # Head of the list

    def append(self, data):
        """Append a new node with the given data to the list."""
        new_node = Node(data)  # Create a new node
        if not self.head:
            self.head = new_node  # If list is empty, set head to new node
            return
        last = self.head  # Start at the head
        while last.next:
            last = last.next  # Traverse to the last node
        last.next = new_node  # Append new node

    def find_max(self) -> int:
        """Find and return the maximum element in the linked list."""
        if not self.head:
            raise ValueError("Cannot find max in an empty list")
        max_value = self.head.data  # Start with the head value
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data  # Update max if current is larger
            current = current.next  # Move to the next node
        return max_value

# Example usage of linked list
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print(ll.find_max())  