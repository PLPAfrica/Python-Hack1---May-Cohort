# Node class to represent each element in the linked list
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

# LinkedList class to manage the nodes
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int):
        new_node = Node(value)  # Create a new node
        if not self.head:  # If the list is empty, set the new node as the head
            self.head = new_node
        else:  # Otherwise, find the last node and append the new node
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Append the new node at the end

    def find_max(self) -> int:
        if not self.head:
            raise ValueError("List is empty")  # Handle empty list case
        
        max_value = self.head.value  
        current = self.head.next
        while current:  
            if current.value > max_value:
                max_value = current.value
            current = current.next  
        
        return max_value

ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())
