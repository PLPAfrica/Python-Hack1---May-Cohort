def reverse_string(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    return reversed_string

# Example usage
if __name__ == "__main__":
    print(reverse_string("Ann"))  # Output: "nnA"
