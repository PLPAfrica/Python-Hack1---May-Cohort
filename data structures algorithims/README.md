
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

### 02queue_stacks.py

This file contains the `QueueStacks` class, which simulates a queue using two stacks. The class provides the following methods:

- **`enqueue(x: int)`**: Adds an element to the queue.
- **`dequeue() -> int`**: Removes and returns the front element of the queue.

#### Example Usage:
```python
from queue_stacks import QueueStacks

queue = QueueStacks()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 20
```

### 03linked_list_max.py

This file contains the `LinkedList` class, which represents a singly linked list. It provides a method `find_max()` to find the maximum element in the list. The file also includes the `Node` class used to build the linked list.

#### Example Usage:
```python
from linked_list_max import LinkedList

ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4
```

## How to Run Tests

Since the files are modular and don't contain print statements or direct execution code, the best way to test them is to import the classes or functions into a Python script or interactive environment (e.g., Python shell, Jupyter Notebook).

To run the example usage:
1. Create a Python script or use an interactive Python environment.
2. Import the necessary classes or functions.
3. Instantiate the objects or call the functions with your test inputs.

## Project Structure

```plaintext
data_structures_algorithms/
├── 01reverse_string.py    # Contains the reverse_string function
├── 02queue_stacks.py      # Contains the QueueStacks class
└── 03linked_list_max.py   # Contains the LinkedList class and Node class
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your proposed changes. All contributions are welcome!

## Author

- [Cynthia Wahome](https://github.com/CynthiaWahome)

---
