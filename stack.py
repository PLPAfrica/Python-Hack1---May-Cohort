class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None  # Handle the case where the stack is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None  # Handle the case where the stack is empty

    def is_empty(self):
        return len(self.items) == 0

    def get_all(self):
        return self.items
