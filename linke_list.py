class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None    

class LinkedList:
    def __init__(self):
        self.head = None  # Starting an empty list

    def append(self, value: int):
        new_node = Node(value)
        if self.head is None:
            # If the list is empty, the new node is set as the head
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        if self.head is None:
            raise ValueError("List is empty")
        
        # Initializing max_value with the value of the head node
        max_value = self.head.value
        current = self.head
        
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value

# Example
def linked_list_example():
    linked_list = LinkedList()
    linked_list.append(120)
    linked_list.append(230)
    linked_list.append(52)
    linked_list.append(115)
  
    print("The maximum value in the linked list is:", linked_list.find_max())  # Output: 20

    
linked_list_example()
