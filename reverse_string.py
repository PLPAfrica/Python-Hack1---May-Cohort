class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

def reverse_string(s: str) -> str:
    stack = Stack()
    
    # push all characters from s to stack
    for char in s:
        stack.push(char)
    
    # pop all elements from stack and append to reversed_s
    reversed_s = ""
    while not stack.is_empty():
        reversed_s += stack.pop()
    
    return reversed_s
