class TwoStackQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def add(self, value: int):
        self.input_stack.append(value)

    def remove(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        
        if self.output_stack:
            return self.output_stack.pop()
        else:
            raise IndexError("Queue is empty. Cannot perform 'remove' operation.")

# Example usage
if __name__ == "__main__":
    queue = TwoStackQueue()
    queue.add(10)
    queue.add(20)
    print(queue.remove())  # Should output 10
