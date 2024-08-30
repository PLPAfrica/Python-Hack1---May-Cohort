# This class defines a stack data structure.
class Stack:
    # initializes the stack
    def __init__(self):
        self.items = []

    # checks if the stack is empty
    def is_empty(self):
        return len(self.items) == 0
    
    
    # adds an item to the top of the stack by appending it to the end of the list
    def push(self, item):
        self.items.append(item)

    # Removes and returns the top item from the stack if it's not empty, or returns None if the stack is empty.
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

# This function reverses a string using a stack and returns the reversed string.
def reverse_string(s):
    
    # The stack is initialized.It iterates through each character in the string, pushing them onto the stack.
    stack = Stack()
    for char in s:
        stack.push(char)

    # The reversed string is created by popping each character from the stack in reverse order
    # and appending it to a new string.
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

# The main() function provides the user to interactively input a string and see the reversed result..
def main():
    
    # User prompted to enter a string.
    string = input("Enter a string to reverse: ")
    
    # The reverse_string() function is called with the user's input.
    reversed_string = reverse_string(string)
    
    # The reversed string is printed to the console.
    print("Reversed string:", reversed_string)

if __name__ == "__main__":
    main()