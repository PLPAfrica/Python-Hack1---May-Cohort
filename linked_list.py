class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data of the node
        self.next = None  # Initialize the next pointer as None
        
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None
    
    def append(self, data):
        # Insert a new node at the end of the list
        new_node = Node(data)   # Create a new node with the given data
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node  # Point the last node's next to the new node
        
    def display(self):
        # Check if the list is empty
        if self.head is None:
            raise ValueError("Cannot display in an empty list")

        # Print the linked list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("End")  # End of the list
        
    def find_max(self) -> int:
        # Check if the list is empty
        if self.head is None:
            raise ValueError("Cannot find maximum value in an empty list")

        # Initialize temp to start from the head of the list
        temp = self.head
        
        # Initialize max_value to the data of the first node
        max_value = temp.data
        
        # Traverse the linked list
        while temp:
            # If the current node's data is greater than max_value, update max_value
            if temp.data > max_value:
                max_value = temp.data
            
            # Move to the next node in the list
            temp = temp.next
        
        # Return the maximum value found in the list
        return max_value
        
list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(4)
list1.append(2)
list1.display()
print("The maximum element in the list is", list1.find_max())