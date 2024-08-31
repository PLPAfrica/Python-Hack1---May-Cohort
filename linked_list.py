class Node:
    def _init_(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
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
            raise ValueError("List is empty")
        
        max_element = self.head.data
        current = self.head
        while current:
            if current.data > max_element:
                max_element = current.data
            current = current.next
        
        return max_element

# Example usage
if __name__ == "_main_":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print(ll.find_max())  # Output: 4