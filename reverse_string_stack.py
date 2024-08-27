def reverse_string(s: str) -> str:
    stack = []

    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)

    reversed_string = ''

    # Pop characters from the stack and append to reversed_string
    while stack:
        reversed_string += stack.pop()

    return reversed_string


# Example usage:
if __name__ == "__main__":
    input_str = "hello"
    output_str = reverse_string(input_str)
    print(output_str)  # Output: "olleh"
