def reverse_string(s: str) -> str:
    # Create an empty stack to hold characters
    stack = []

    # Push each character onto the stack
    for char in s:
        stack.append(char)
    
    reversed_str = ''

    # Pop characters from the stack to reverse the string
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Usage
input_string = "How are you doing?"
output_string = reverse_string(input_string)
print(output_string)  

#Output
#?gniod uoy era woH
