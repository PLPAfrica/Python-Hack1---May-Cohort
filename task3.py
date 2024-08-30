class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.max_value = float('-inf')

    def append(self, value: int):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.max_value = max(self.max_value, value)

    def find_max(self) -> int:
        return self.max_value


ll = LinkedList()
ll.append(20)
ll.append(5)
ll.append(1)
ll.append(60)
print(ll.find_max())  # Output: 60
