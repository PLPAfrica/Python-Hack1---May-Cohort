def reverse_string(s: str) -> str:
    #use a list as a stack to store characters
    stack = []

    #Push each character of the input string onto the stack
    for char in s:
        stack.append(char)

    #Initialize an empty string to store the reversed string    
    reversed_str = ""

    #Pop each character from the stack and append it to the reversed string
    while stack:
        reversed_str += stack.pop()
        
    #return the reversed string
    return reversed_str

#test the function
input_str = input("Enter a one worded string: ")
output_str = reverse_string(input_str)

print(f"Input: {input_str}")
print(f"Output: {output_str}")
    