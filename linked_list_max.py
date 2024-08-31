class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head_node = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head_node:
            self.head_node = new_node
        else:
            current_node = self.head_node
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
    
    def find_max(self) -> int:
        if not self.head_node:
            raise ValueError("The linked list is empty")
        
        max_value = self.head_node.value
        current_node = self.head_node.next_node
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next_node
        
        return max_value

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(15)
    linked_list.append(5)
    linked_list.append(25)
    linked_list.append(10)
    print(linked_list.find_max())  
    # Output: 25
