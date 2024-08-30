#1. Reverse a String Using a Stack

class Stack:    
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from an empty stack")

        # Return the item at the top of the stack without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def reverse_string(s: str) -> str:
    stack = Stack()
    for char in s:
        stack.push(char)

    # Initialize an empty string to store the reversed result
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

# Example 1
greeting = "hello"
reversed_greeting = reverse_string(greeting)  
print(f"Original greeting: {greeting}")  
print(f"Reversed greeting: {reversed_greeting}")  


# Example 2
name = "Ampofua"
reversed_name = reverse_string(name)  
print(f"Original name: {name}")  
print(f"Reversed name: {reversed_name}")  


# Example 3
game_name = "basketball"
reversed_game_name = reverse_string(game_name)  
print(f"Original game name: {game_name}")  
print(f"Reversed game name: {game_name}")  



