# A stack is a data structure that follows the Last In, First Out (LIFO) principle.


# We start by creating a function that will actually reverse the string. 

def reverse_string(s: str) -> str:
    # We first initialize an empty stack.
    stack = []
    
    # We loop through each character in the input string 's'
    for char in s:
        # Add the character to the stack using the append property
        stack.append(char)
    
    # Now we initialize an empty string to store the reversed result
    reversed_str = ""
    
    # Popping from the stack will give us the characters in reverse order
    while stack:  # While the stack is not empty
        # Remove the top character from the stack and add it to the reversed string
        reversed_str += stack.pop()
    
    # Step 5: Return the reversed string
    return reversed_str

# Let's request input from the user and convert it's data type to string to make this program awesome.
input_string = str(input("Enter a word: \n"))
output_string = reverse_string(input_string)

# Output the reversed string
print(output_string)
