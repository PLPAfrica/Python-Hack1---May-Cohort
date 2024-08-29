# Data Structures and Algorithms Practice Hackathon

This repository contains solutions to three simple data structures and algorithms problems. Please follow the instructions below to complete the tasks and submit your work.

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

# Solutions

### 1. Reverse a String Using a Stack


This Python code demonstrates how to reverse a string using a stack data structure.

## Code Explanation

1. **`Stack` Class:**
   - This class implements a basic stack data structure.
   - `__init__`: Initializes an empty list `self.items` to store the stack elements.
   - `push(item)`: Adds an `item` to the top of the stack (appends to the list).
   - `pop()`: Removes and returns the top element from the stack (pops from the list). It handles an empty stack condition.
   - `is_empty()`: Checks if the stack is empty.

2. **`reverse_string(s)` Function:**
   - Takes a string `s` as input and reverses it using a stack.
   - **Input Validation:** Raises a `ValueError` if the input is not a string.
   - **Stack Operations:**
     - Creates a `Stack` object.
     - Pushes each character of the input string onto the stack.
     - Pops characters from the stack and adds them to a list to build the reversed string.
   - **Return Value:** Returns the reversed string as a single string.

3. **`interactive_string_reversal()` Function:**
   - Provides a user-friendly interface for string reversal.
   - Prompts the user to enter a string.
   - Handles the "quit" command to exit the program.
   - Calls `reverse_string` to reverse the input and displays the original, reversed, and palindrome check results.
   - Catches `ValueError` exceptions for invalid input.

4. **`if __name__ == "__main__":` Block:**
   - Ensures that `interactive_string_reversal()` is called only when the script is run directly, not when imported as a module.

### Time and Space Complexity

- **`reverse_string`:**
   - **Time Complexity:** O(n), where n is the length of the input string (linear time due to iterating through the string and pushing/popping elements from the stack).
   - **Space Complexity:** O(n), where n is the length of the input string (the stack stores all characters of the input).

### Usage

1. Run the script.
2. Enter a string to reverse.
3. The program will display the original string, the reversed string, and whether the original string is a palindrome.
4. Type "quit" to exit the program.

### 2. Implement a Queue Using Two Stacks

This  code implements a queue data structure using two stacks. This approach allows for efficient enqueue operations and amortized O(1) dequeue operations.

## Code Explanation

### 1. `Stack` Class:

- This class provides a basic implementation of a stack data structure.
- `__init__`: Initializes an empty list `self.items` to store the stack elements.
- `push(item)`: Adds an `item` to the top of the stack (appends to the list).
- `pop()`: Removes and returns the top element from the stack (pops from the list). It raises an `IndexError` if the stack is empty.
- `peek()`: Returns the top item from the stack without removing it. It raises an `IndexError` if the stack is empty.
- `is_empty()`: Checks if the stack is empty.
- `size()`: Returns the number of items in the stack.

### 2. `QueueWithStacks` Class:

- This class implements a queue using two stacks:
    - `stack_newest`:  A stack to store newly added elements.
    - `stack_oldest`: A stack to store elements ready to be dequeued.
- `__init__`: Initializes the two stacks.
- `enqueue(x)`: Adds an element `x` to the back of the queue by pushing it onto `stack_newest`.
- `dequeue()`: Removes and returns the front element of the queue. This involves:
    - Shifting elements from `stack_newest` to `stack_oldest` if `stack_oldest` is empty (using the `_shift_stacks` helper method).
    - Popping the top element from `stack_oldest`.
- `peek()`: Returns the front element of the queue without removing it. It also involves shifting elements if necessary.
- `is_empty()`: Checks if the queue is empty.
- `size()`: Returns the total number of elements in the queue.
- `_shift_stacks()`: This private method moves elements from `stack_newest` to `stack_oldest` if `stack_oldest` is empty. This ensures that the oldest element is always available at the top of `stack_oldest`. It raises an `IndexError` if both stacks are empty (i.e., the queue is empty).
- `display()`: Prints the elements in the queue from front to back.

### 3. `interactive_queue_demo()` Function:

- This function provides an interactive demonstration of the `QueueWithStacks` implementation.
- It presents a menu of queue operations: enqueue, dequeue, peek, is_empty, size, display, and exit.
- Users can interact with the queue by choosing from these options.

### 4. `if __name__ == "__main__":` Block:

- Ensures that `interactive_queue_demo()` is called only when the script is run directly, not when imported as a module.

### Time and Space Complexity

- **`QueueWithStacks`:**
    - **Enqueue:** O(1) (constant time).
    - **Dequeue:** Amortized O(1) (constant time on average). In the worst case (when `stack_oldest` is empty), it takes O(n) time to shift all elements from `stack_newest` to `stack_oldest`, where `n` is the number of elements in the queue. However, this worst-case scenario happens only once for each `n` elements enqueued.
    - **Peek:** Amortized O(1) (same reasoning as dequeue).
    - **is_empty()**: O(1) (constant time).
    - **size()**: O(1) (constant time).
    - **Space Complexity:** O(n) (linear space, as the stacks store all the elements of the queue).

### Usage

1. Run the script.
2. The program will present a menu of queue operations.
3. Choose an operation by entering the corresponding number.
4. Follow the prompts to perform the chosen operation.
5. Enter '7' to exit the program.

### 3. Find the Maximum Element in a List Using a Linked List

This Python code implements a basic singly linked list data structure.

## Code Explanation

### 1. `Node` Class:

- Represents a single node in the linked list.
- `__init__(data)`: Initializes a node with given `data` and sets its `next` pointer to `None` (initially pointing to no other node).

### 2. `LinkedList` Class:

- Represents the entire linked list.
- `__init__()`: Initializes an empty linked list by setting its `head` to `None`.
- `append(data)`: Appends a new node with the given `data` to the end of the list.
    - Creates a new `Node` object with the given data.
    - If the list is empty, sets the new node as the `head`.
    - Otherwise, traverses to the last node in the list and sets its `next` pointer to the new node.
- `find_max()`: Finds and returns the maximum element in the linked list.
    - If the list is empty, returns `None`.
    - Initializes `max_value` with the data of the first node.
    - Traverses the list, updating `max_value` whenever a larger element is encountered.
- `display()`: Displays all elements in the linked list.
    - Traverses the list, collecting all elements into a list.
    - Prints the elements as a string, or "Empty list" if the list is empty.

### 3. `interactive_linked_list()` Function:

- Provides an interactive interface for users to manipulate a linked list and demonstrate its functionality.
- Presents a menu of linked list operations: append, find maximum, display, and exit.
- Users can interact with the list by choosing from these options.

### 4. `if __name__ == "__main__":` Block:

- Ensures that `interactive_linked_list()` is called only when the script is run directly, not when imported as a module.

### Time and Space Complexity

- **`append(data)`:**
    - **Time Complexity:** O(n) (linear time), where `n` is the number of nodes in the list. This is because we need to traverse the list to find the last node.
    - **Space Complexity:** O(1) (constant space). We are only creating a new node and modifying pointers, not allocating additional memory proportional to the size of the list.
- **`find_max()`:**
    - **Time Complexity:** O(n) (linear time), as we need to traverse the entire list to find the maximum element.
    - **Space Complexity:** O(1) (constant space). We are only storing a few variables, not allocating additional memory proportional to the list size.
- **`display()`:**
    - **Time Complexity:** O(n) (linear time) for traversing the list.
    - **Space Complexity:** O(n) (linear space) because we are storing all the elements in a list for display.

### Usage

1. Run the script.
2. The program will present a menu of linked list operations.
3. Choose an operation by entering the corresponding number.
4. Follow the prompts to perform the chosen operation.
5. Enter '4' to exit the program.


