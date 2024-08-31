class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    stack = Stack()
    for char in s:
        stack.push(char)
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str

# Example usage:
if __name__ == "__main__":
    print(reverse_string("world"))  # Output: "dlrow"
