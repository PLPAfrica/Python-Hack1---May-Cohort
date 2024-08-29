# Class Node:
class Node:
    def __init__(self, data: int): # __init__(self, data: int): Initialize data with the given value and next as None.
        self.data = data
        self.next = None

# Class LinkedList:
class LinkedList:
    def __init__(self):     # __init__(self): Initialize head as None (empty list).
        self.head = None

    def append(self, data: int): # append(self, data: int):
        new_node = Node(data)   # Create a new node.
        if self.head is None:
            self.head = new_node    # If head is None, set head to the new node.
        else:
            current = self.head
            while current.next is not None:
                current = current.next  # Otherwise, traverse to the end and add the new node.
            current.next = new_node

    def find_max(self) -> int:  # find_max(self) -> int:
        if self.head is None:
            raise ValueError("The linked list is empty.")   # If head is None, raise an exception.

        max_value = self.head.data  # Initialize max_value with head.data.
        current = self.head.next

        while current is not None:
            if current.data > max_value:
                max_value = current.data    # Traverse the list, updating max_value when a larger value is found.
            current = current.next

        return max_value    # Return max_value.



ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4