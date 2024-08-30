def reverse_string(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Example :
input_string = input("Which country are you from?")
reversed_string = reverse_string(input_string)
print(f"Original String: {input_string}")
print(f"Reversed String: {reversed_string}")


