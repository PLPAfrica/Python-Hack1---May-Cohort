# Reverse a String Using a Stack

This project demonstrates how to reverse a string using a stack data structure in Python.

## Problem Statement

You need to reverse a given string using a stack. A stack is a data structure that follows the Last In, First Out (LIFO) principle, meaning the last element added to the stack is the first one to be removed. By leveraging this behavior, you can reverse a string by pushing each character onto the stack and then popping them off in reverse order.

## Code Explanation

The `reverse_string` function takes a string `s` as input and returns the reversed string. Here’s how the function works:

1. **Create a Stack**: A stack is simulated using a Python list. We initialize an empty list named `stack`.

2. **Push Characters to Stack**: We iterate over each character in the input string and push it onto the stack using the `append` method.

3. **Pop Characters from Stack**: We initialize an empty string named `reversed_string`. Then, we enter a loop where we pop characters from the stack one by one and add them to `reversed_string`. Since the stack follows LIFO, this results in the characters being added in reverse order.

4. **Return the Reversed String**: Finally, the function returns the `reversed_string`.

### Example

```bash
$ python reverse_string.py
```
