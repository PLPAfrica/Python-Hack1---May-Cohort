def reverse_string(str):
    string_stack = [char for char in str]
    reversed_string_stack = []
    while len(string_stack) > 0:
        reversed_string_stack.append(string_stack.pop())
    reversed_string = ''.join(reversed_string_stack)
    return reversed_string

string = input("Enter a string: ")
print(f"Reversed string: {reverse_string(string)}")