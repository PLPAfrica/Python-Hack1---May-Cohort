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
            # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            # Traverse to the end of the list
            current = self.head
            while current.next:
                current = current.next
            # Append the new node at the end
            current.next = new_node

    def find_max(self) -> int:
        
        if self.head is None:
            # If the list is empty, return None
            return None
        
        max_value = self.head.value  
        current = self.head
        
        # Traverse the list to find the maximum value
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value

# Example usage
li = LinkedList()
li.append(3)  
li.append(6)
li.append(312)  
li.append(84)  
li.append(34)   

# Find and print the maximum value in the linked list
print("The maximum element in the linked list is:", li.find_max())
