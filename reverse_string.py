class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    stack = Stack()
    
    for char in s:
        stack.push(char)
    
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

# Test the function
if __name__ == "__main__":
    input_str = "hello"
    output_str = reverse_string(input_str)
    print(f"Input: {input_str}")
    print(f"Output: {output_str}")
