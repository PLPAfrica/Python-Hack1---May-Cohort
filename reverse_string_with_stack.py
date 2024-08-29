from stack import Stack

def reverse_string(val):
    stack = Stack()
    
    # Push characters of the string onto the stack
    for char in val:
        stack.push(char)
    
    updated_str = ""
    
    # Pop characters from the stack and form the reversed string
    while not stack.is_empty():
        updated_str += stack.pop()
        
    return updated_str

name = "Geoffrey"
print(reverse_string(name))  # Output: yreferoG
