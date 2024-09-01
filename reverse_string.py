def reverse_string(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

if __name__ == "__main__":
    test_string = "live"
    result = reverse_string(test_string)
    print(f"Original string: {test_string}")
    print(f"Reversed string: {result}")
