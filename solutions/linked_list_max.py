class Node:
    def __init__(self, data: int):
        self.data = data # Stores the value of the node
        self.next = None # Points to the next node in the list

class LinkedList: 
    def __init__(self):
        self.head = None # Points to the first node in the list

    def append(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        if not self.head:
            raise ValueError("The linked list is empty.") # Handle empty list
        
        max_value = self.head.data
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value # Return the maximum value found

#Usage
ll = LinkedList()
ll.append(10)
ll.append(5)
ll.append(8)
ll.append(12)
ll.append(7)

print(ll.find_max())  

# Output
# 12

