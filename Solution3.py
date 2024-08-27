class Node:
    def __init__(self, value: int):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        if self.head is None:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
    
li = LinkedList()
li.append(45)
li.append(9)
li.append(23)
li.append(54)
li.append(2)

print("The maximum element in the linked list is:", (li.find_max()))