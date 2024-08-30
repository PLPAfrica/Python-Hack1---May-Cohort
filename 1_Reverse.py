## The stack will follow the Last In, First Out (LIFO) principle, which makes it suitable for reversing.
def reverse_string(s: str) -> str:
    stack = []
    
    # Push all characters of the string into the stack
    for char in s:
        stack.append(char)
    
    reversed_str = ""
    
    # Pop characters from the stack to form the reversed string
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"
