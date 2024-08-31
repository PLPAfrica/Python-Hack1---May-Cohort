def reverse_string(s: str) -> str:
    """
    Reverses the input string using a stack.

    Parameters:
    s (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    # Step 1: Initialize an empty stack
    stack = []

    # Step 2: Push each character of the string onto the stack
    for char in s:
        stack.append(char)

    # Step 3: Pop characters from the stack to create the reversed string
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()

    return reversed_str


# Step 4: Asking user to insert a string and then print its reverse form
input_string = input("Enter any string and you will get its reverse form: ")
output_string = reverse_string(input_string)
print(f"You inserted: {
      input_string}\nThe reverse form of your input is: {output_string}")
