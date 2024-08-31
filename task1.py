#Reverse a String Using a Stack
def reverse_string(s: str) -> str: #the function (s: str) expects a string as input and the function (-> str) will return a string
    stack = []
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    reversed_string = ''
    
    # Pop all characters from the stack and form the reversed string
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string


input_string = "Hello!"
reversed_string = reverse_string(input_string)
print("Initial String:", input_string)
print("Reversed String:", reversed_string)
