# Question 1
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from an empty stack")

def reverse_string(s: str) -> str:
    stack = Stack()
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.push(char)
    
    # Pop all characters from the stack and build the reversed string
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

def main():
    # Prompt user for input
    user_input = input("Enter a string to reverse: ")
    
    # Reverse the string
    reversed_string = reverse_string(user_input)
    
    # Output the reversed string
    print(f"Reversed string: {reversed_string}")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()

    