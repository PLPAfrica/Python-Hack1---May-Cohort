# 1. Reverse a String Using a Stack

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
    reversed_string = ""


    for char in s:
        stack.push(char)


    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

#Example
print(reverse_string("hello")) 