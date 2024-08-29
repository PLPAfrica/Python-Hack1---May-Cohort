# Define the Node class that represents each element in the linked list
class Node:
    def __init__(self, value: int):
        # Each node has some data (in this case, an integer) and a pointer to the next node
        self.value = value
        self.next = None

# Define the LinkedList class that manages the entire list
class LinkedList:
    def __init__(self):
        # The list starts off empty, so the head (first node) is initially None
        self.head = None

    def append(self, value: int):
        """
        Add a new element to the end of the linked list.
        :param value: The integer value to be added to the list.
        """
        # Create a new node with the given value
        new_node = Node(value)
        # If the list is empty, the new node becomes the head
        if not self.head:
            self.head = new_node
        else:
            # Otherwise, find the last node and link it to the new node
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def find_max(self) -> int:
        """
        Traverse the linked list to find and return the maximum value.
        :return: The maximum integer value in the list.
        :raises ValueError: If the list is empty.
        """
        # If the list is empty, we can't find a maximum value
        if not self.head:
            raise ValueError("The linked list is empty. Add some elements first!")

        # Assume the head's value is the maximum initially
        max_value = self.head.value
        current_node = self.head.next
        
        # Traverse through the list, updating max_value if a larger value is found
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        
        return max_value

# Example usage
if __name__ == "__main__":
    # Create an empty linked list
    linked_list = LinkedList()

    # Append elements to the linked list
    linked_list.append(3)
    linked_list.append(1)
    linked_list.append(4)
    linked_list.append(2)

    # Find and print the maximum value in the linked list
    max_value = linked_list.find_max()
    print(f"The maximum value in the linked list is: {max_value}")  
