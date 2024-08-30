def reverse_string(my_string):
    # Initialize an empty list to use as a stack
    stack = []

    # Push each character of the string onto the stack
    for char in my_string:
        stack.append(char)

    # Pop characters from the stack and append to the reversed string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    return reversed_string

my_string = "My name is James"
reversed_string = reverse_string(my_string)
print(f"Original string: {my_string}")
print(f"Reversed string: {reversed_string}")