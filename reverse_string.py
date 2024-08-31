def reverse_string(input_string: str) -> str:
    # Initialize an empty list to use as a stack for character storage
    reverse_stack = []
    # Initialize an empty string to accumulate the reversed characters
    reversed_string = ""

    # Loop through each character in the input string
    for character in input_string:
        # Append each character to the stack
        reverse_stack.append(character)

    # Continue popping characters from the stack until it's empty
    while reverse_stack:
        # Pop the last character from the stack and add it to the reversed string
        reversed_string += reverse_stack.pop()
        
    # Return the fully constructed reversed string
    return reversed_string

# Prompt the user for input to reverse
input_string = input("Enter the string you would like to reverse: ")

# Call the reverse_string function with the user's input
reversed_string = reverse_string(input_string)

# Print the resulting reversed string
print("The reversed string is", reversed_string)