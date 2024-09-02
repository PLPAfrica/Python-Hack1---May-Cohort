def reverse_string(s: str) -> str:
    # Initialize an empty stack
    stack = []

    # Push each character of the string onto the stack
    for char in s:
        stack.append(char)

    # Pop characters from the stack and build the reversed string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# Example usage:
input_string = "hello"
output_string = reverse_string(input_string)
print(output_string)  # Output: "olleh"
