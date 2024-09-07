# Define the class to be tested
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        if not self.head:
            raise ValueError("Empty list")
        
        max_value = self.head.value
        current = self.head.next  # Start from the second node
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value

# Define test functions for LinkedList
def test_linked_list():
    ll = LinkedList()  # Correct instantiation
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    assert ll.find_max() == 4  # Test for the highest value
    print("test_linked_list passed!")



#Run the test

if __name__=="__main__":
    test_linked_list()
    print("linked_list test passed!")
