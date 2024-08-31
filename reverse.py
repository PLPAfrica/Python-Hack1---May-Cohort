def reverse_string(s: str) -> str:
    stack = []

    # Push all characters in stack
    for char in s:
        stack.append(char)

    # Pop characters to get them in reverse order
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# Example usage
input_string = "hello"
output_string = reverse_string(input_string)
print("Input:", input_string)
print("Output:", output_string)
