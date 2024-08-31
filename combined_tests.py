from reverse_string import reverse_string
from queue_with_stacks import TwoStackQueue
from linked_list_max import SinglyLinkedList

# Test for reverse_string function
def test_reverse_string():
    assert reverse_string("hello") == "olleh", "Test Case 1 Failed: Expected 'olleh'"
    assert reverse_string("world") == "dlrow", "Test Case 2 Failed: Expected 'dlrow'"
    assert reverse_string("") == "", "Test Case 3 Failed: Expected '' for empty string"  # Edge case: Empty string
    assert reverse_string("a") == "a", "Test Case 4 Failed: Expected 'a' for single character"  # Edge case: Single character
    assert reverse_string("12345") == "54321", "Test Case 5 Failed: Expected '54321' for numerical string"
    print("All reverse_string test cases passed!")

# Test for TwoStackQueue class
def test_two_stack_queue():
    queue = TwoStackQueue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    assert queue.remove() == 1, "Test Case 1 Failed: Expected 1"
    assert queue.remove() == 2, "Test Case 2 Failed: Expected 2"
    queue.add(4)
    assert queue.remove() == 3, "Test Case 3 Failed: Expected 3"
    assert queue.remove() == 4, "Test Case 4 Failed: Expected 4"
    try:
        queue.remove()
        assert False, "Test Case 5 Failed: Should have raised IndexError"
    except IndexError:
        pass  # Expected behavior
    print("All TwoStackQueue test cases passed!")

# Test for SinglyLinkedList class
def test_singly_linked_list():
    linked_list = SinglyLinkedList()
    linked_list.add_node(3)
    linked_list.add_node(1)
    linked_list.add_node(4)
    linked_list.add_node(2)
    assert linked_list.find_maximum_value() == 4, "Test Case 1 Failed: Expected 4"
    
    linked_list = SinglyLinkedList()  # Test with an empty list
    try:
        linked_list.find_maximum_value()
        assert False, "Test Case 2 Failed: Should have raised ValueError for empty list"
    except ValueError:
        pass  # Expected behavior

    linked_list.add_node(-10)
    linked_list.add_node(-20)
    assert linked_list.find_maximum_value() == -10, "Test Case 3 Failed: Expected -10 for negative values"

    print("All SinglyLinkedList test cases passed!")

if __name__ == "__main__":
    test_reverse_string()
    test_two_stack_queue()
    test_singly_linked_list()
