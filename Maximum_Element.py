# Finding the Maximum Element in a List Using a Linked List

class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def find_max(self) -> int:
        if not self.head:
            return None

        max_element = self.head.data
        current_node = self.head.next
        while current_node:
            if current_node.data > max_element:
                max_element = current_node.data
            current_node = current_node.next

        return max_element

# Its Usage
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
ll.append(10)
print(ll.find_max()) #Prints 10 as the maximum value