    ## SOLUTIONS TO THE ALGORITHMS
    ## Reversing a string using a stack

- A stack is a data structure that follows the Last in, First OUT(LIFO) principle, meaning that the last item you put in the stack is the first one you get out. i.e when you place a chair on top of a stack, and you want a chair you take the top one first.
  *Steps to reverse a string using a stack.
  1. You initialize the stack, like creating an empty stack.
  2. Then one can push the characters on to the stack, as each character is added it goes to the top.
  3. Pop characters from the stack- the characters will be removed one by one(pop), this will give the characters in reverse order.
  4. Building the reversed string - as we pop each character from the stack, we append it to a new string, This new string will be the reversed version of the original string.

  * How the stack works
  * initial string "hello"
  * The Push Phase;
    - Push 'h' → Stack: ['h']
    - Push 'e' → Stack: ['h', 'e']
    - Push 'l' → Stack: ['h', 'e', 'l']
    - Push 'l' → Stack: ['h', 'e', 'l', 'l']
    - Push 'o' → Stack: ['h', 'e', 'l', 'l', 'o']
  * The Pop Phase
    - Pop → 'o', Stack: ['h', 'e', 'l', 'l'], Reversed String: 'o'
    - Pop → 'l', Stack: ['h', 'e', 'l'], Reversed String: 'ol'
    - Pop → 'l', Stack: ['h', 'e'], Reversed String: 'oll'
    - Pop → 'e', Stack: ['h'], Reversed String: 'olle'
    - Pop → 'h', Stack: [], Reversed String: 'olleh'
  * Now the final reversed string becomes ("olleh")


    ## Implementing a Queue Using Two Stacks
- A queue is a data structure that follows the First In, First Out (FIFO) principle, meaning that the first element added to the queue is the first one to be removed, similar to a line of people waiting to be served.
- A stack, on the other hand, follows the Last In, First Out (LIFO) principle, where the last element added is the first one to be removed.
  * How it works- 
    * Two stacks:
     - Two stacks are used, 'stack1' and 'stack2', to manage the queue operations.
    * Enqueueing the Operation (Adding to the Queue):
     - When an element is enququed, its simply pushed on 'stack1', and that stack will hold all the elements in the order they were added.
    * Dequeueing the Operations (Removing from the Queue):
     - When an element is dequed, the element that was added first is removed first.
     - If 'stack2' is empty, all elements from 'stack1' are popped and pushed to 'stack2'. This reverses the order of elements such that the oldest element becomes the one that is on top of 'stack2'.
     - Then the top element is popped from 'stack2', which represents the front of the queue.
  * Representation
  - Initial State:
    - stack1: []
    - stack2: []
  - Enqueue 1:
    - stack1: [1]
    - stack2: []
  - Enqueue 2:
    - stack1: [1, 2]
    - stack2: []
  - Dequeue (Transfer elements from stack1 to stack2 and pop):
    - Transfer → stack1: [], stack2: [2, 1]
    - Pop → stack2: [2], Output: 1
  - Enqueue 3:
    - stack1: [3]
    - stack2: [2]
  - Dequeue (Pop from stack2):
    - Pop → stack2: [], Output: 2
* Output Example
   - Enqueue 1: stack1 becomes [1]
   - Enqueue 2: stack1 becomes [1, 2]
   - Dequeue:
      - stack1 is transferred to stack2, making stack2 [2, 1].
      - The first element (1) is popped from stack2, so the output is 1.
   - Enqueue 3: stack1 becomes [3].
   - Dequeue:
      - The next element (2) is popped from stack2, so the output is 2.
   - Dequeue:
      - Since stack2 is empty, stack1 is transferred to stack2, and 3 is   popped. The output is 3.

## Finding the Maximum Element in a List Using a Singly Linked List
  - A linked list is a datastructure consisting of nodes where each node contains data and a reference to the next node in the sequence.
  - Linked lists do not store elements in contagious memory locations unlike arrays making them more flexible but slightly more complex to work with.
        - solving the solution
  * create a singly linked list - a type of linked list where each node points to the next node and the last node points to none, indicating the end of the list.
  * Traverse the Linked List - comparing node values with the current maximum value.
  * Find the Maximum Element - when we find a hihgher value we keep track of it and keep updating if we find another higher value.
  













































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
