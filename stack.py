class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

def reverse_string(s: str) -> str:
    # Initializing a stack
    stack = Stack()
    
    # Pushing all characters of the string into the stack
    for char in s:
        stack.push(char)
    
    # Poping characters from the stack and build the reversed string
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

input_string = "hassan"
print(reverse_string(input_string)) 

class QueueWithStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    # Adding an element to the end of the queue
    def enqueue(self, x: int):
        self.in_stack.append(x)

    # Removing and returning the front element of the queue
    def dequeue(self) -> int:
        if not self.out_stack:  # Transfer elements only if out_stack is empty
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        # If out_stack is still empty, the queue is empty
        if not self.out_stack:
            raise IndexError("dequeue from empty queue")
        
        return self.out_stack.pop()


queue = QueueWithStacks()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print(queue.dequeue())  
print(queue.dequeue())  
print(queue.dequeue())  
print(queue.dequeue())  