def reverse_string(s: str) -> str:
    #Reverse the input string using a stack.#
    stack = []

    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)

    # Pop characters from the stack to reverse the string
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# This example prompts the user to input the string they want to reverse and it out puts the reversed string:
if __name__ == "__main__":
    # Prompt the user for input
    input_str = input("Enter a string to reverse: ")

    # Reverse the input string
    reversed_str = reverse_string(input_str)

    # Print the reversed string
    print(f"Reversed string: '{reversed_str}'")


  