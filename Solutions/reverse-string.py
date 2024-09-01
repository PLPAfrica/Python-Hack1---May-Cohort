class ReverseString:
    def reverse_string(self, s: str) -> str:
        stack = []
        for char in s:
            stack.append(char)
        
        reversed_str = ""
        while stack:
            reversed_str += stack.pop()
        
        return reversed_str
