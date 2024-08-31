class Stack:
    def _init_(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_s = ""
    while not stack.is_empty():
        reversed_s += stack.pop()
    
    return reversed_s

# Example usage
if __name__ == "_main_":
    input_str = "hello"
    output_str = reverse_string(input_str)
    print(output_str)  # Output: "olleh"