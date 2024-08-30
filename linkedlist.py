class Node:
# Represents a single node in a singly linked list.
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def find_max(self):
        if self.head is None:
            return None  # Empty list has no maximum

        max_element = self.head.data
        current_node = self.head.next
        while current_node:
            max_element = current_node.data if current_node.data > max_element else max_element
            current_node = current_node.next
        return max_element
    
#  Example usage
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())