

## Overview

This repository contains solutions to three fundamental data structures and algorithms problems. Each problem is implemented with a focus on clean code, efficiency, fault tolerance, and thorough documentation.

### 1. Reverse a String Using a Stack

- **Function:** `reverse_string(s: str) -> str`
- **Description:** Reverses the input string using a stack data structure.
- **Example:**
  python
 print(reverse_string("hello"))  # Output: "olleh"
  

### 2. Implement a Queue Using Two Stacks

- **Class:** `QueueWithStacks`
- **Methods:**
  - `enqueue(x: int)`: Adds an element to the queue.
  - `dequeue() -> int`: Removes and returns the front element of the queue.
- **Example:**
 python
  q = QueueWithStacks()
  q.enqueue(1)
  q.enqueue(2)
  print(q.dequeue())  # Output: 1
  print(q.dequeue())  # Output: 2
  

### 3. Find the Maximum Element in a List Using a Linked List

- **Class:** `LinkedList`
- **Method:**
  - `find_max() -> int`: Finds and returns the maximum element in the list.
- **Example:**
  python
  ll = LinkedList()
  ll.append(3)
  ll.append(1)
  ll.append(4)
  ll.append(2)
  print(ll.find_max())  # Output: 4
## Code Quality

The solutions are designed with clean, readable code, ensuring correctness and efficiency. Each solution includes error handling for robustness and detailed inline comments for maintainability.

## License

This repository is licensed under the MIT License.


### Final Touches

- *Test Cases:* Write additional test cases to cover edge cases and validate the correctness of each solution.
- *Optimize the Code:* Double-check for any potential optimizations in your code.
- *Refactor if Needed:* If there are any redundant or unclear parts, refactor the code to improve readability and performance.
