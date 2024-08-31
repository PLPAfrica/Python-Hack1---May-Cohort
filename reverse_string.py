class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

def reverse_string(s: str) -> str:
    stack = Stack()
    reversed_str = ""

    # Push all characters of the string onto the stack
    for char in s:
        stack.push(char)

    # Pop all characters from the stack and append them to the result
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

# Example usage:
print(reverse_string("hello"))  
