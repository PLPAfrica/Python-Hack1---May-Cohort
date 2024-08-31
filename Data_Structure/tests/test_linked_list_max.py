from src.linked_list_max import LinkedList

def test_linked_list_find_max():
    """
    This function tests the find_max method of a LinkedList class.

    The LinkedList class is assumed to have the following methods:
    - append(value): Adds a new node with the given value to the end of the list.
    - find_max(): Returns the maximum value in the list. If the list is empty, raises a ValueError.

    Raises:
        AssertionError: If the find_max method does not return the expected maximum value 
        or does not raise a ValueError for an empty list.
    """

    # Create and populate a LinkedList
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.append(25)
    ll.append(65)

    # Print appended items
    def print_list(linked_list):
        items = []
        current_node = linked_list.head
        while current_node:
            items.append(current_node.data)
            current_node = current_node.next
        return items
    
    print(f"LinkedList items: {print_list(ll)}")

    # Find and print the maximum value
    max_value = ll.find_max()
    print(f"Maximum Value in LinkedList: {max_value}")  # Display maximum value
    assert max_value == 65, f"Expected 65 but got {max_value}"

    # Test find_max with an empty LinkedList
    try:
        empty_ll = LinkedList()
        empty_ll.find_max()
        assert False, "Did not raise ValueError for empty linked list"
    except ValueError as e:
        print(f"Error for empty LinkedList: {e}")  # Display error message

if __name__ == "__main__":
    test_linked_list_find_max()
    print("All LinkedList find_max tests passed!")
