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
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def find_max(self):
        node1 = self.head
        node2 = node1.next
        while node2.next:
            if node1.data > node2.data:
                max = node1.data
            else:
                max = node2.data
            node1 = node1.next
            node2 = node1.next
        return max
    
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())