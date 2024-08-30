class Stack:
    def __init__(self):
        
        self.items = [] 

    def push(self, item):
       
        self.items.append(item)  

    def pop(self):
        
        return self.items.pop()  

    def is_empty(self):
        
        return len(self.items) == 0  

def reverse(s: str) -> str:
   
    stack = Stack()  
    # Push each character of the string onto the stack
    for char in s:
        stack.push(char)

    reversed_str = ''  
    # Pop each character from the stack and append to the reversed string
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str  

# Example usage
value = input("Enter any string of your choice:")  
print(reverse(value))  
