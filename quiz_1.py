def reverse_string(s: str) -> str:
    # Creating a stack (using a list)
    stack = []
    
    # Pushing  all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Poping characters from the stack and build the reversed string
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str


input_str = "hello"
print(reverse_string(input_str)) 

