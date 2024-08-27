def reverse_string(s: str) -> str:
    # Create an empty stack
    stack = []
    
    # Push all characters onto the stack
    for char in s:
        stack.append(char)
    
    # Pop characters from the stack and form the reversed string
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str


input_string = "hello"
output_string = reverse_string(input_string)
print(output_string)  # Output: "olleh"
