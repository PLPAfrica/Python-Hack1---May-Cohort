# Define the function to be tested
def reverse_string(s: str) -> str:
    return s[::-1]  # Simple implementation using slicing

# Define test functions
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    print("test_reverse_string passed")

# Define the class to be tested
class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("dequeue from empty queue")
        return self.stack2.pop()

# Define test functions
def test_queue_with_stacks():
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    print("test_queue_with_stacks passed")

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

# Run all tests
if __name__ == "__main__":
    test_reverse_string()
    test_queue_with_stacks()
    test_linked_list()
    print("All tests passed!")
