from solutions import reverse_string, QueueWithStacks, LinkedList

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"

def test_queue_with_stacks():
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2

def test_linked_list():
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    assert ll.find_max() == 4

if __name__ == "__main__":
    test_reverse_string()
    test_queue_with_stacks()
    test_linked_list()
    print("All tests passed!")
