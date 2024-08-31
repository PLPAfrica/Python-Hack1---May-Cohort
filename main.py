from reverse_string import reverse_string
from queue_with_stacks import QueueWithStacks
from linked_list import LinkedList

def main():
    # Task 1: Reverse a String Using a Stack
    input_str = "hello"
    output_str = reverse_string(input_str)
    print(output_str)  # Output: "olleh"

    # Task 2: Implement a Queue Using Two Stacks
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2

    # Task 3: Find the Maximum Element in a List Using a Linked List
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print(ll.find_max())  # Output: 4

if __name__ == "_main_":
    main()