class Node:
    def __init__(self, data):
        """
        Initialize a new node with given data and next pointer as None.
        
        :param data: The data to be stored in the node.
        """
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.size = 0

    def append(self, data):
        """
        Append a new node with the specified data to the end of the list.
        
        :param data: The data to be added to the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        self.size += 1

    def prepend(self, data):
        """
        Insert a new node with the specified data at the beginning of the list.
        
        :param data: The data to be added to the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def find_max(self) -> int:
        """
        Find the maximum value in the linked list.
        
        :return: The maximum value in the list.
        :raises ValueError: If the list is empty.
        """
        if not self.head:
            raise ValueError("List is empty")
        max_val = self.head.data
        current = self.head
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val

    def delete(self, data):
        """
        Delete the first occurrence of the specified data from the list.
        
        :param data: The data to be removed from the list.
        :raises ValueError: If the data is not found in the list.
        """
        if not self.head:
            raise ValueError("List is empty")
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            raise ValueError(f"Data {data} not found in the list")
        
        current.next = current.next.next
        self.size -= 1

    def display(self):
        """
        Display the contents of the linked list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def get_size(self) -> int:
        """
        Get the number of elements in the linked list.
        
        :return: The size of the linked list.
        """
        return self.size

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    
    print("Linked List Elements:", ll.display())  # Output: [3, 1, 4, 2]
    print("Maximum Value:", ll.find_max())  # Output: 4
    
    ll.prepend(5)
    print("Linked List after Prepend:", ll.display())  # Output: [5, 3, 1, 4, 2]
    
    ll.delete(1)
    print("Linked List after Deletion:", ll.display())  # Output: [5, 3, 4, 2]
    
    print("Size of Linked List:", ll.get_size())  # Output: 4
