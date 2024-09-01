class Node:
    def __init__(self, data):
        # Initialize a node with data and a pointer to the next node
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize the head of the linked list
        self.head = None

    def append(self, data):
        # Add a new node with the given data to the end of the list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def find_max(self) -> int:
        # Find the maximum element in the linked list
        if not self.head:
            raise ValueError("The linked list is empty")
        
        max_value = self.head.data
        current_node = self.head
        
        while current_node:
            if current_node.data > max_value:
                max_value = current_node.data
            current_node = current_node.next
        
        return max_value


ll = LinkedList()
ll.append(3)
ll.append(5)
ll.append(2)
ll.append(8)
ll.append(1)

print(ll.find_max())