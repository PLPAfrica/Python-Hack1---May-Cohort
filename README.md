
---

# Data Structures and Algorithms Practice

This repository contains solutions to three fundamental data structure and algorithm problems implemented in Python. Each solution is modular and can be integrated into larger projects or tested in an interactive Python environment.

## Overview

The repository contains the following files:

1. **`01reverse_string.py`**: Implements a stack-based approach to reverse a string.
2. **`02queue_stacks.py`**: Implements a queue using two stacks.
3. **`03linked_list_max.py`**: Implements a singly linked list and provides a method to find the maximum element in the list.

## Requirements

- Python 3.x

## Files and Functionality

### 01reverse_string.py

This file contains the `reverse_string` function, which reverses a given string using a stack-based approach.

#### Example Usage:
```python
from reverse_string import reverse_string

result = reverse_string("hello")
print(result)  # Output: "olleh"
```

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
