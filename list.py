class Node:
    def __init__(self, data: int):
        self.data = data  # Node's data
        self.next = None  # Pointering to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # The head (start) of the linked list

    # Method to add a new node at the end of the linked list
    def insert(self, data: int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traversing to the end of the list
                current = current.next
            current.next = new_node

    # Method to find the maximum element in the linked list
    def find_max(self) -> int:
        if self.head is None:
            raise ValueError("The list is empty.")
        
        max_value = self.head.data  # Initializing max_value to the first node's data
        current = self.head

        # Traversing the linked list to find the max value
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value


linked_list = LinkedList()
linked_list.insert(20)
linked_list.insert(70)
linked_list.insert(11)
linked_list.insert(9)
linked_list.insert(30)

print(linked_list.find_max())