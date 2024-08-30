def reverse_string(s: str) -> str:
    """
    Reverse a given string using a stack.

    Args:
    s (str): The string to reverse.

    Returns:
    str: The reversed string.
    """
    stack = []

    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)

    # Pop characters from the stack to get them in reverse order
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string