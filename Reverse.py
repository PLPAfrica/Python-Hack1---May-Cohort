def reverse_string(s: str) -> str:
#   Reverses a string using a stack.

#   Args:
#     s: The input string.
#   Returns:
#     The reversed string.
#   

  stack = []
  for char in s:
    stack.append(char)

  reversed_str = ""
  while stack:
    reversed_str += stack.pop()

  return reversed_str

# Example usage:
string_to_reverse = "hello, world!"
reversed_string = reverse_string(string_to_reverse)
print(reversed_string)  # Output: !dlrow ,olleh