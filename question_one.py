stack = []
def reverse_string(s: str) -> str:
            
    for char in s:
        stack.append(char)
        print(stack)
                
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
                
    return reversed_str
print(f'Reverse String :{reverse_string("hello")}')  # Output: "olleh"
   

