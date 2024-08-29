class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class QueueWithStacks:
    def __init__(self):
        self.stack_newest = Stack()
        self.stack_oldest = Stack()

    def enqueue(self, x: int) -> None:
        self.stack_newest.push(x)

    def dequeue(self) -> int:
        self._shift_stacks()
        return self.stack_oldest.pop()

    def peek(self) -> int:
        self._shift_stacks()
        return self.stack_oldest.peek()

    def is_empty(self) -> bool:
        return self.stack_newest.is_empty() and self.stack_oldest.is_empty()

    def size(self) -> int:
        return self.stack_newest.size() + self.stack_oldest.size()

    def _shift_stacks(self) -> None:
        if self.stack_oldest.is_empty():
            while not self.stack_newest.is_empty():
                self.stack_oldest.push(self.stack_newest.pop())

        if self.stack_oldest.is_empty():
            raise IndexError("Queue is empty")

    def display(self) -> None:
        if self.is_empty():
            print("Queue is empty")
        else:
            elements = list(self.stack_oldest.items) + list(reversed(self.stack_newest.items))
            print("Front ->", " <- ".join(map(str, elements)), "<- Back")


def interactive_queue_demo():
    q = QueueWithStacks()
    
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Is Empty?")
        print("5. Size")
        print("6. Display Queue")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        try:
            if choice == '1':
                value = int(input("Enter value to enqueue: "))
                q.enqueue(value)
                print(f"{value} enqueued successfully")
            elif choice == '2':
                value = q.dequeue()
                print(f"Dequeued value: {value}")
            elif choice == '3':
                value = q.peek()
                print(f"Front of the queue: {value}")
            elif choice == '4':
                print(f"Is queue empty? {q.is_empty()}")
            elif choice == '5':
                print(f"Queue size: {q.size()}")
            elif choice == '6':
                q.display()
            elif choice == '7':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except IndexError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    interactive_queue_demo()6