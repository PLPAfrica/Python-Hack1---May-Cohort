class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def find_max(self) -> int:
        if not self.head:
            raise ValueError("List is empty")
        
        max_value = self.head.data
        current = self.head.next
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(13)
    ll.append(11)
    ll.append(14)
    ll.append(12)
    print("The maximum value in the list is:", ll.find_max())  #14 will be the output
