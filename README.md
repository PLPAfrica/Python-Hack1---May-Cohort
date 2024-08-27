Data structures and Algorithms Practice

1. Reverse a String Using a Stack
Task: Implement a stack data structure to reverse a string.

Approach: A stack is a Last-In-First-Out (LIFO) data structure which is ideal for reversing a string. We can push each character of the string onto the stack, and then pop each character to build the reversed string.

Implementation:

reverse_stack.py

Explanation:

Stack Class: A basic stack implementation with push, pop, and is_empty methods.
reverse_string Function: Pushes each character of the input string onto the stack and then pops from the stack to build the reversed string.

2. Implement a Queue Using Two Stacks
Task: Implement a queue using two stacks.

Approach: To simulate a queue using two stacks, we use one stack (stack_in) for enqueue operations and another stack (stack_out) for dequeue operations. When dequeuing, we transfer elements from stack_in to stack_out if stack_out is empty.

Implementation:

queue_two_stacks.py

Explanation:

QueueWithStacks Class: Manages two stacks: stack_in for adding elements and stack_out for removing elements.
enqueue Method: Adds elements to stack_in.
dequeue Method: Transfers elements from stack_in to stack_out if stack_out is empty, then pops from stack_out.

3. Find the Maximum Element in a List Using a Linked List
Task: Implement a singly linked list and find the maximum element in the list.

Approach: A singly linked list allows us to traverse elements linearly. We can traverse the list while keeping track of the maximum value encountered.

Implementation:

reverse_stack.py

Explanation:

Node Class: Represents a node in the linked list with a value and a reference to the next node.
LinkedList Class: Manages the linked list with methods to append nodes and find the maximum value.
find_max Method: Traverses the list while keeping track of the highest value.



