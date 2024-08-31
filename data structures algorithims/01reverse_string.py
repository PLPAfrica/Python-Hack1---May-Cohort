"""Implement a stack data structure to reverse a string. """

def reverse_string(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_str = ""    
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

