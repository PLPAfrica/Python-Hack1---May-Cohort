class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    stack = Stack()
    
    # Push all characters onto the stack
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    
    # Pop all characters from the stack to form the reversed string
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test
input_string = "hello"
output_string = reverse_string(input_string)
print(f"Input: {input_string}")
print(f"Output: {output_string}")