## Questions

### 1. Reverse a String Using a Stack
# - **Task:** Implement a stack data structure to reverse a string.
# - **Function:** `reverse_string(s: str) -> str`
def reverse_string(s:str) -> str:
    stack =list(s)
    reverse_str =''
    while stack:
        reverse_str += stack.pop()
    return reverse_str
input_str="hello"   
output_str= reverse_string(input_str)
print(output_str)

# ### 2. Implement a Queue Using Two Stacks
# - **Task:** Implement a queue using two stacks.
# - **Class:** `QueueWithStacks`
# - **Methods:**
#   - `enqueue(x: int)`: Adds an element to the queue.
#   - `dequeue() -> int`: Removes and returns the front element of the queue.
# - **Example:**
#   ```python
#   q = QueueWithStacks()
#   q.enqueue(1)
#   q.enqueue(2)
#   print(q.dequeue())  # Output: 1
#   print(q.dequeue())  # Output: 2


class QueueWithStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueue
        self.stack2 = []  # Stack for dequeue

    def enqueue(self, x: int):
        self.stack1.append(x)  # Add element to Stack1

    def dequeue(self) -> int:
        if not self.stack2:  # If Stack2 is empty, refill it
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None  # Remove from Stack2
    # - **Explanation:** We use two stacks to implement a queue. The `enqueue` operation is
    #   simply adding an element to the first stack. The `dequeue` operation is more
    #   complex. If the second stack is empty, we need to transfer all elements from the
    #   first stack to the second stack. Then we can remove the top element from the
    #   second stack.
    # Example usage
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2


# ### 3. Find the Maximum Element in a List Using a Linked List
# - **Task:** Implement a singly linked list and find the maximum element in the list.
# - **Class:** LinkedList
# - **Method:** find_max() -> int
# - **Example**
#   ```python
#   ll = LinkedList()
#   ll.append(3)
#   ll.append(1)
#   ll.append(4)
#   ll.append(2)
#   print(ll.find_max())  # Output: 4
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        if not self.head:
            return None

        max_value = self.head.data
        current = self.head.next

        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value

# Example usage
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4