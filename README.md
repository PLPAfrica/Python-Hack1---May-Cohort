# Data Structures and Algorithms Practice

This repository contains solutions to three simple data structures and algorithms problems:

Reverse a String Using a Stack
Implement a Queue Using Two Stacks
Find the Maximum Element in a List Using a Linked List

## How to Use the Code

To use the code, simply clone this repository and run the Python files using a Python interpreter.

## Solutions and Implementations

Task 1: Reverse a String Using a Stack
The reverse_string function uses a stack data structure to reverse a string. It pushes each character of the string onto a stack, then pops each character off the stack to build the reversed string.

Task 2: Implement a Queue Using Two Stacks
The QueueWithStacks class implements a queue using two stacks. The enqueue method adds an element to the queue by pushing it onto stack1. The dequeue method removes and returns the front element of the queue by popping all elements from stack1 and pushing them onto stack2, then popping the top element from stack2.

Task 3: Find the Maximum Element in a List Using a Linked List
The LinkedList class implements a singly linked list, and the find_max method finds the maximum element in the list by iterating through the list and keeping track of the maximum element.

## How to Run the Code

To run the code, simply execute the Python files using a Python interpreter. For example, you can run the reverse_string function using the following command:


python -c "from reverse_string import reverse_string; print(reverse_string('hello'))"
This will output the reversed string "olleh".

Similarly, you can run the QueueWithStacks class using the following command:


python -c "from queue_with_stacks import QueueWithStacks; q = QueueWithStacks(); q.enqueue(1); q.enqueue(2); print(q.dequeue()); print(q.dequeue())"
This will output the dequeued elements 1 and 2.

Finally, you can run the LinkedList class using the following command:

python -c "from linked_list import LinkedList; ll = LinkedList(); ll.append(3); ll.append(1); ll.append(4); ll.append(2); print(ll.find_max())"
This will output the maximum element 4.

If you also prefer running the code all at once you can use the following command:
python data_structures_practice.py

# Note

## This code assumes that you have Python 3.x installed on your system.























### Submission Instructions
- Fork this repository.
- Clone the forked repository to your local machine.
- Create a separate branch for your solutions.
- Implement the solutions to the above questions in Python.
- Commit your changes with clear and descriptive messages.
- Push your changes to your forked repository.
- Create a pull request (PR) to the original repository with your solutions.
- Submit the URL of your GitHub repository as your final submission.

### Submission form 
https://forms.gle/VUTFyWTXKUPq4CMQA
