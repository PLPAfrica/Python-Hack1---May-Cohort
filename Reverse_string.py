
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
    
    # Push character 
    for char in s:
        stack.push(char)
    
    # Pop  character
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

# Example 
if __name__ == "__main__":
    input_string = "Python is really interesting"
    reversed_string = reverse_string(input_string)
    print("Original String:", input_string)
    print("Reversed String:", reversed_string)
