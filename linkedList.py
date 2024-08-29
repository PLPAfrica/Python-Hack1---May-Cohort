# Class Node:
# __init__(self, data: int): Initialize data with the given value and next as None.

# Class LinkedList:
# __init__(self): Initialize head as None (empty list).
# append(self, data: int):
# Create a new node.
# If head is None, set head to the new node.
# Otherwise, traverse to the end and add the new node.
# find_max(self) -> int:
# If head is None, raise an exception.
# Initialize max_value with head.data.
# Traverse the list, updating max_value when a larger value is found.
# Return max_value.

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        if self.head is None:
            raise ValueError("The linked list is empty.")

        max_value = self.head.data
        current = self.head.next

        while current is not None:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value


ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4
