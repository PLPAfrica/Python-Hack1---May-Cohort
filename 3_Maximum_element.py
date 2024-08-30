## Implement a singly linked list and then find the maximum element.
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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def find_max(self) -> int:
        if not self.head:
            return None  # List is empty
        
        max_value = self.head.data
        current_node = self.head
        
        # Traverse the list and find the maximum value
        while current_node:
            if current_node.data > max_value:
                max_value = current_node.data
            current_node = current_node.next
        
        return max_value

# Example usage:
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4
