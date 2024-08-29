### 1. Reverse a String Using a Stack
def reverse_string(s: str) -> str:
    # Initialize an empty stack (list in this case)
    stack = []
    
    # Push each character of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Initialize an empty string to hold the reversed string
    reversed_str = ""
    
    # Pop each character from the stack and add it to the reversed string
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage:
input_string = "hello"
output_string = reverse_string(input_string)
print(output_string)  # Output: "olleh"
