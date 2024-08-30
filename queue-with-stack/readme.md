# Queue Implementation Using Two Stacks

This project demonstrates how to implement a queue using two stacks in Python. A queue is a data structure that follows the First In, First Out (FIFO) principle, meaning the first element added to the queue will be the first one to be removed.

## Overview

In this implementation, we use two stacks to mimic the behavior of a queue. The key idea is to use one stack (`stack_in`) to handle all enqueue (insertion) operations and the other stack (`stack_out`) to handle dequeue (removal) operations.

## How It Works

### Enqueue Operation

When an element is added to the queue using the `enqueue(x)` method, it is pushed onto `stack_in`. This stack keeps track of the order in which elements are added.

### Dequeue Operation

When an element is removed from the queue using the `dequeue()` method, the following steps occur:

1. If `stack_out` is empty, all elements from `stack_in` are popped and pushed onto `stack_out`. This reverses the order of elements, making the oldest element (the first one added) available at the top of `stack_out`.

2. The element at the top of `stack_out` is popped and returned, following the FIFO principle.

### Example

Here is an example to demonstrate how the queue works:

```python
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
```
