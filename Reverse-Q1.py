def reverse_string(s: str) -> str:
    # Initialize an empty stack
    stack = []
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Pop characters from the stack to get the reversed string
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage
if __name__ == "__main__":
    input_string = "hello"
    print(f"Original string: {input_string}")
    print(f"Reversed string: {reverse_string(input_string)}")