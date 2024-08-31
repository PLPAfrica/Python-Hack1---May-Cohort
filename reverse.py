class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def is_empty(self):
        return len(self.stack) == 0

def reverse_string(s: str) -> str:
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage:
if __name__ == "__main__":
    s = "hello"
    print(reverse_string(s))  # Output: "olleh"
