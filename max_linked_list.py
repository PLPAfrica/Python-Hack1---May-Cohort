class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    
    def find_max(self) -> int:
        if not self.head:
            raise ValueError("The linked list is empty")
        max_value = self.head.data
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(7)
    ll.append(15)
    ll.append(2)
    ll.append(9)
    print(ll.find_max())  

