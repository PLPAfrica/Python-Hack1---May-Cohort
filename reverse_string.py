def reverse_string(s: str) -> str:
    stack =[]
    for char in s:
        stack.append(char)
    reverse_string = ""
    while stack:
        reverse_string += stack.pop()
    return reverse_string

print(reverse_string("name"))  