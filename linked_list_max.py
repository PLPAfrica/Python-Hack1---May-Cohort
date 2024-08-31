class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next_node = None

class SinglyLinkedList:
    def __init__(self):
        self.head_node = None

    def add_node(self, value: int):
        new_node = ListNode(value)
        if self.head_node is None:
            self.head_node = new_node
        else:
            current = self.head_node
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def find_maximum_value(self) -> int:
        if self.head_node is None:
            raise ValueError("Cannot find maximum in an empty list.")
        
        max_value = self.head_node.value
        current = self.head_node.next_node
        
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            current = current.next_node
        
        return max_value

