# Define a function to reverse a string
def reverse_string(s: str) -> str:
    
    # Create a list to hold characters
    stack = []
    
    # Push all characters of the string to the list(stack) created
    for char in s:
        stack.append(char)
    
    # Pop all characters from the stack and form the reversed string
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage
if __name__ == "__main__":
    input_string = "casmir"
    print(reverse_string(input_string))  # Output: "rimsac"
