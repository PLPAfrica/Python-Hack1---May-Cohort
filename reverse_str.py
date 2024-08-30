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

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)


def reverse_string(input_str):

    # Initialize stack
    stack = Stack()

    # Push all characters of the input string onto the stack
    for char in input_str:
        stack.push(char)

    # Pop all characters from the stack and append to reversed_str
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str


# Test the reverse_string function
print(reverse_string("hello"))
