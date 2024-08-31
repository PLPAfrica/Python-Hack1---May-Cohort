def reverse_string(s: str) -> str:
    stack = []
    
    # Push each character of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Pop each character from the stack and build the reversed string
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

input_string = "hello"
output_string = reverse_string(input_string)
print(output_string)
