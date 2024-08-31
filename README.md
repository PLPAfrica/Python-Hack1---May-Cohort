Data Structures and Algorithms Solutions
Overview
This repository contains solutions for three fundamental data structures and algorithms challenges implemented in Python. The challenges demonstrate the use of stacks, queues, and linked lists to solve common problems.

Challenges

1. Reverse a String Using a Stack
   Task: Implement a stack-based approach to reverse a string.

Function: reverse_string(s: str) -> str

Description: This solution utilizes a stack to reverse the characters of a given string. By pushing each character onto the stack and then popping them off, the characters are retrieved in reverse order.

Example:

    input_str = "hello"
    print(reverse_string(input_str))  # Output: "olleh"

2. Implement a Queue Using Two Stacks
   Task: Implement a queue using two stacks to manage enqueue and dequeue operations.

Class: QueueWithStacks

Methods:

enqueue(x: int): Adds an element to the queue.
dequeue() -> int: Removes and returns the front element of the queue.
Description: This implementation uses two stacks to simulate the behavior of a queue. Elements are added to one stack and removed from another, allowing FIFO (First-In-First-Out) order to be maintained.

Example:

    queue = QueueWithStacks()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.dequeue())  # Output: 1
    print(queue.dequeue())  # Output: 2

3. Find the Maximum Element in a Linked List
   Task: Implement a singly linked list and find the maximum element.

Class: LinkedList

Method: find_max() -> int

Description: This solution involves implementing a singly linked list where nodes store integer values. The find_max method traverses the list to find and return the maximum value.

Example:

    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.append(1)
    linked_list.append(4)
    linked_list.append(2)
    print(linked_list.find_max())  # Output: 4

Requirements
Python 3.x
How to Run
Clone the repository:

    git clone <repository-url>

Navigate to the repository directory:

    cd <repository-directory>

Run the Python files to execute the solutions:

    python <file-name>.py

License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/<jdamour12>/<Python-Hack1---May-Cohort/tree/jdamour-branch>/blob/main/LICENSE) file for details.
