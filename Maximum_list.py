class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        if self.head is None:
            raise ValueError("The list is empty")
        
        max_value = self.head.data
        current = self.head
        while current is not None:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value

# Example
if __name__ == "__main__":
    linked_list = LinkedList()
    numbers = [15, 17, 19, 21, 23] 

    for number in numbers:
        linked_list.append(number)

    max_value = linked_list.find_max()
    print("The maximum value in the linked list is:", max_value)
