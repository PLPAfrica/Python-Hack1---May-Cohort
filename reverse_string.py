def reverse_string(s: str) -> str:
    # initialization of the empty stack
    stack = []

    # pushing the characters of the string to the stack
    for char in s:
        stack.append(char)

    # popping the characters from the stack so as to build the reversed string
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()

    return reversed_str


# testing the function
input_str = 'hello'
output_str = reverse_string(input_str)
print(f"The input is: {input_str} ")
print(f"The output is: {output_str} ")