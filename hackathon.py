# 1. Reverse a string using a stack
def reverse_string(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)