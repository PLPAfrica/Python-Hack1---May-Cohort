def reverse_string(s: str) -> str:
    # Create an empty stack
    stack = []

    # Push characters in the string into the stack
    for char in s:
        stack.append(char)

     # Initialize as an empty string
    reversed_string = ""  

    # Pop each character from the stack and append it to the reversed string
    while stack:
        reversed_string += stack.pop()
    
    # Return the reversed string
    return reversed_string  

    #user input

user_input = input("Please enter a string to reverse: ")

reversed_output = reverse_string(user_input)

    # Print the reversed string
print(f"Reversed string: {reversed_output}")


