class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find_max(self):
        """
        Finds the maximum element in the linked list.

        Returns:
            int: The maximum element in the list.
        """
        if not self.head:
            return None
        max_element = self.head.data
        current = self.head.next
        while current:
            if current.data > max_element:
                max_element = current.data
            current = current.next
        return max_element

# Example usage:
linked_list = LinkedList()
linked_list.append(50)
linked_list.append(10)
linked_list.append(37)
linked_list.append(20)
linked_list.append(15)

print(linked_list.find_max())  