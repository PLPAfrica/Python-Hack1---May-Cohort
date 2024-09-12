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

  readme/Steps explanations

Original file line number	Diff line number	Diff line change
@@ -0,0 +1,17 @@
Task 1: Reverse a String Using a Stack
Explanation;
Stack Class: Implements a basic stack with methods to push items, pop items, and check if the stack is empty.
reverse_string Function:Initializes a stack.Pushes each character of the input string onto the stack.Pops each character from the stack to build the reversed string.
The stack follows Last In, First Out (LIFO) order, so when characters are popped from the stack, they come out in reverse order of their input.
Task 2: Implement a Queue Using Two Stacks
Explanation;
QueueWithStacks Class:Uses two stacks (stack1 and stack2) to simulate queue operations.
enqueue Method: Adds an element to stack1.
dequeue Method:If stack2 is empty, moves all elements from stack1 to stack2 (reversing their order).Pops and returns the top element from stack2. If both stacks are empty, raises an exception.
This method allows the queue to maintain FIFO order by reversing the order of elements between the two stacks.
Task 3. Find the Maximum Element in a List Using a Linked List
Explanation
Node Class: Represents a node in the linked list with a value and a pointer to the next node.
LinkedList Class:
append Method: Adds a new node to the end of the list.
find_max Method:Traverses the linked list from the head to find and return the maximum value.


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
