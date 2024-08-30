def reverse_string(s: str) -> str:
    
    
    stack = []
    reversed_s = ""
    
    # Push characters onto the stack
    for char in s:
        stack.append(char)
    
    # Pop characters off the stack to build the reversed string
    while stack:
        reversed_s += stack.pop()
    
    return reversed_s

#  usage
input_str =input("Enter word: ")
output = reverse_string(input_str)
print(f"Reversed : {output}")
