# Data Structures and Algorithms Practice

This repository contains your solutions to three simple data structures and algorithms problems. Please follow the instructions below to complete the tasks and submit your work.

## Questions

### 1. Reverse a String Using a Stack

- **Task:** Implement a stack data structure to reverse a string.
- **Function:** `reverse_string(s: str) -> str`
- **Example:**
  - Input: `"hello"`
  - Output: `"olleh"`

### 2. Implement a Queue Using Two Stacks

- **Task:** Implement a queue using two stacks.
- **Class:** `QueueWithStacks`
- **Methods:**
  - `enqueue(x: int)`: Adds an element to the queue.
  - `dequeue() -> int`: Removes and returns the front element of the queue.
- **Example:**
  ```python
  q = QueueWithStacks()
  q.enqueue(1)
  q.enqueue(2)
  print(q.dequeue())  # Output: 1
  print(q.dequeue())  # Output: 2
  ```

### 3. Find the Maximum Element in a List Using a Linked List

- **Task:** Implement a singly linked list and find the maximum element in the list.
- **Class:** LinkedList
- **Method:** find_max() -> int
- **Example**
  ```python
  ll = LinkedList()
  ll.append(3)
  ll.append(1)
  ll.append(4)
  ll.append(2)
  print(ll.find_max())
  ```

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

## SOLUTION AND DOCUMENTATION

## Python Data Structures and Algorithms

Overview
This repository contains implementations of fundamental data structures and algorithms in Python, including a singly linked list and a queue implemented using two stacks.

Linked List
Description
The LinkedList class represents a singly linked list where each element (node) contains an integer value and a reference to the next node in the list.

Features
Appending Elements: Add new nodes to the end of the list.
Finding Maximum Value: Traverse the list to find and return the maximum value.
Example
python
Copy code

# Create a linked list and append elements

linked_list = LinkedList()
linked_list.append(3)
linked_list.append(1)
linked_list.append(4)
linked_list.append(2)

# Find and print the maximum value in the linked list

max_value = linked_list.find_max()
print(f"The maximum value in the linked list is: {max_value}")
Implementation
python
Copy code
class Node:
def **init**(self, value: int):
self.value = value
self.next = None

class LinkedList:
def **init**(self):
self.head = None

    def append(self, value: int):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def find_max(self) -> int:
        if not self.head:
            raise ValueError("The linked list is empty. Add some elements first!")

        max_value = self.head.value
        current_node = self.head.next

        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next

        return max_value

Queue with Two Stacks
Description
The QueueWithStacks class implements a queue using two stacks. Elements are enqueued onto one stack and dequeued from the other, with transfer operations as needed.

Features
Enqueue: Add elements to the end of the queue.
Dequeue: Remove and return elements from the front of the queue.
Example
python
Copy code

# Create a queue and perform operations

q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue()) # Output: 1
print(q.dequeue()) # Output: 2
Implementation
python
Copy code
class QueueWithStacks:
def **init**(self):
self.stack_in = []
self.stack_out = []

    def enqueue(self, x: int):
        self.stack_in.append(x)

    def dequeue(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        if not self.stack_out:
            raise IndexError("Dequeue from an empty queue")

        return self.stack_out.pop()

How to Contribute
Fork the repository and clone it to your local machine.
Create a new branch:
bash
Copy code
git checkout -b feature/your-feature
Make your changes and commit:
bash
Copy code
git add .
git commit -m "Add your descriptive commit message"
Push your branch:
bash
Copy code
git push origin feature/your-feature
Create a pull request from your feature branch to the main branch.
License
This project is licensed under the MIT License. See the LICENSE file for details.
