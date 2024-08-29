def reverse_string(s: str) -> str:
    stack = []  # Step 1: Create an empty list to use as a stack
    
    # Step 2: Push all characters of the string onto the stack
    for char in s:
        stack.append(char) 
    
    reversed_string = ''  # Step 3: Create an empty string to store the reversed characters
    
    # Step 4: Pop characters from the stack and add to the reversed_string
    while stack: 
        reversed_string += stack.pop() 
    
    return reversed_string

print(reverse_string("hello"))