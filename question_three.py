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
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        return new_node
    
    def find_max(self) -> int:
        if not self.head:
            raise ValueError("List is empty")
        max_value = self.head.data
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(f'Maximum Element is: {ll.find_max()}')  # Output: 4
