### 1. Reverse a String Using a Stack
def reverse_string(s: str) -> str:
    # Initialize an empty stack (list in this case)
    stack = []
    
    # Push each character of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Initialize an empty string to hold the reversed string
    reversed_str = ""
    
    # Pop each character from the stack and add it to the reversed string
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage:
input_string = "hello"
output_string = reverse_string(input_string)
print(output_string)  # Output: "olleh"

### 2. Implement a Queue Using Two Stacks
class QueueWithStacks:
    def __init__(self):
        # Two stacks to simulate the queue behavior
        self.stack_in = []  # Stack to handle incoming elements
        self.stack_out = []  # Stack to handle outgoing elements

    def enqueue(self, x: int):
        # Push element onto the stack_in
        self.stack_in.append(x)

    def dequeue(self) -> int:
        # If stack_out is empty, move elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        # Pop the top element from stack_out, which is the front of the queue
        return self.stack_out.pop() if self.stack_out else None
    