from stack import Stack

def reverse_string(val: str) -> str:
    """
    Reverse the characters of a given string using a stack.

    Args:
        val (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    
    # Instantiate the stack to use its methods
    stack = Stack()

    # Push each character of the string onto the stack
    for char in val:
        stack.push(char)

    updated_str = ""

    # Pop characters from the stack and build the reversed string
    while not stack.is_empty():
        updated_str += stack.pop()

    return updated_str

# Example of Usage
def create_secret_code(user_input: str) -> str:
    """
    Create a secret code by reversing the user's input.

    Args:
        user_input (str): The string to be reversed and used as a secret code.

    Returns:
        str: A message containing the reversed input as the secret code.
    """
    reversed_input = reverse_string(user_input)
    return f"Yey! Your secret code is: {reversed_input}"

# Test
if __name__ == "__main__":
    user_input = "OpenSesame"
    secret_code = create_secret_code(user_input)
    print(secret_code)  # Output: "Yey! Your secret code is: emaseSnepO"
    


