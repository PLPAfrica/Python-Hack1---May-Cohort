# Python Data Structures and Algorithms: Task Solutions
## Overview
This repository contains Python implementations for three different data structure and algorithm tasks. Each task demonstrates a fundamental concept in computer science, focusing on clean code, readability, correctness, efficiency, and fault tolerance.

## Task List
- Reverse a String Using a Stack
- Implement a Queue Using Two Stacks
- Find the Maximum Element in a List Using a Linked List

## Task 1: Reverse a String Using a Stack
### Description
This task involves implementing a stack data structure to reverse a given string. The stack is a Last-In-First-Out (LIFO) data structure, which makes it ideal for reversing the order of characters in a string.

### Function
Function Name: reverse_string(s: str) -> str
Parameters:
s (str): The string to be reversed.
Returns:
A new string with the characters of s in reverse order.


## Example
from stack_reverse_string import reverse_string

input_string = "hello"
output_string = reverse_string(input_string)
print(output_string)  # Output: "olleh"

### How It Works
Push: Each character of the input string is pushed onto a stack.
Pop: Characters are popped from the stack, resulting in the reverse order of the input string.
Key Features
Time Complexity: O(n), where 𝑛  is the length of the string.
Space Complexity: 𝑂 (𝑛) O(n), for storing characters in the stack.

#  File
## stack_reverse_string.py
### Task 2: Implement a Queue Using Two Stacks
#### Description
This task requires implementing a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, and this implementation demonstrates how to simulate a queue using two LIFO stacks.

## Class
Class Name: QueueWithStacks
Methods:
enqueue(x: int): Adds an element x to the end of the queue.
dequeue() -> int: Removes and returns the front element of the queue.

## Example
from queue_with_stacks import QueueWithStacks

q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2


## How It Works

Enqueue Operation: Pushes elements onto the first stack.
Dequeue Operation:
If the second stack is empty, all elements from the first stack are popped and pushed onto the second stack.
The top element of the second stack is then popped and returned.

## Key Features
Time Complexity: enqueue: O(1)
dequeue: Amortized O(1)

Space Complexity:  O(n), where  n is the number of elements in the queue.
#### File
queuewithStacks.py

## queue_with_stacks.py
### Task 3: Find the Maximum Element in a List Using a Linked List
#### Description
This task involves implementing a singly linked list and a method to find the maximum element in the list. A singly linked list is a linear data structure where each element points to the next, forming a chain.

## Class
Class Name: LinkedList
## Methods:
- append(data: int): Adds a new node with the specified data to the end of the list.
- find_max() -> int: Finds and returns the maximum element in the linked list.

### Example
from linked_list_max import LinkedList

ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4

## How It Works
Appending Elements: The append() method traverses to the end of the list and adds a new node.
Finding Maximum: The find_max() method traverses the list, keeping track of the maximum value encountered.
## Key Features
Time Complexity: append: 𝑂(𝑛) where n is the number of nodes in the list.

find_max:  O(n), where  n is the number of nodes in the list.

Space Complexity:   O(1) for both methods, apart from the input data.

#### File
linked_list_max.py


# Getting Started
## Prerequisites
Python 3.x is required to run the scripts.
## Installation
Clone the repository to your local machine:
- git clone https://github.com/yourusername/yourrepository.git
- cd yourrepository

## Usage
Each task is implemented in its respective Python file. To test the functionality, you can run each script individually or import the functions and classes into your own projects.

## Testing
You can test each task by running the corresponding Python script directly. For example, to test the string reversal, use:
- python stack_reverse_string.py

## Contributing
Contributions are welcome! If you have suggestions for improvements, feel free to create a pull request or open an issue.