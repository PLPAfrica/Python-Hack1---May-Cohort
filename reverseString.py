# <!-- Solution -->
#A stack is a linear data structure that stores items in a LIFO manner.
#In this task, we shall be using the same principle by;Pushing each character
#onto the stack, then popping characters from the stack to build the reversed string.


def reverse_string(s: str) -> str:
    stack = []  # Initialize the stack
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    reversed_string = ""  # Initialize the reversed string
    
    # Pop characters from the stack to reverse the string
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"
