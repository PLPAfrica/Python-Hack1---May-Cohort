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
  print(ll.find_max())  # Output: 4


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



# Solution to Data Structures and Algorithms Hackathon

## Overview
This repository contains solutions to the hackathon that are implemented in Python.

## Solutions
1. **Reverse a String Using a Stack**
   - Implemented using a stack to reverse the string.
   - Handles edge cases such as empty strings.

2. **Implement a Queue Using Two Stacks**
   - Uses two stacks to efficiently handle queue operations.
   - Includes error handling for dequeuing from an empty queue.

3. **Find the Maximum Element in a List Using a Linked List**
   - Implements a singly linked list to find the maximum value.
   - Handles the case of an empty linked list.

## How to Run
1. Clone the repository: `git clone <repository-url>`
2. Navigate to the directory: `cd <repository-name>`
3. Run the solutions using Python 3: `python <solution-file>.py`

