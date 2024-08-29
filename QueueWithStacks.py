class Stack:
    """A basic implementation of a Stack data structure."""

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")

    def peek(self):
        """
        Return the top item from the stack without removing it.
        
        Returns:
            The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")

    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Get the number of items in the stack.
        
        Returns:
            int: The number of items in the stack.
        """
        return len(self.items)


class QueueWithStacks:
    """
    An implementation of a Queue using two Stacks.
    This allows for efficient enqueue operations and amortized O(1) dequeue operations.
    """

    def __init__(self):
        """Initialize two empty stacks for the queue implementation."""
        self.stack_newest = Stack()  # Stack for newly added elements
        self.stack_oldest = Stack()  # Stack for elements ready to be dequeued

    def enqueue(self, x: int) -> None:
        """
        Add an element to the back of the queue.
        
        Args:
            x (int): The element to be added to the queue.
        """
        self.stack_newest.push(x)

    def dequeue(self) -> int:
        """
        Remove and return the front element from the queue.
        
        Returns:
            int: The front element of the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        self._shift_stacks()
        return self.stack_oldest.pop()

    def peek(self) -> int:
        """
        Return the front element of the queue without removing it.
        
        Returns:
            int: The front element of the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        self._shift_stacks()
        return self.stack_oldest.peek()

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.stack_newest.is_empty() and self.stack_oldest.is_empty()

    def size(self) -> int:
        """
        Get the number of elements in the queue.
        
        Returns:
            int: The number of elements in the queue.
        """
        return self.stack_newest.size() + self.stack_oldest.size()

    def _shift_stacks(self) -> None:
        """
        Move elements from stack_newest to stack_oldest if stack_oldest is empty.
        This operation is performed to prepare elements for dequeue or peek operations.
        
        Raises:
            IndexError: If both stacks are empty (i.e., the queue is empty).
        """
        if self.stack_oldest.is_empty():
            while not self.stack_newest.is_empty():
                self.stack_oldest.push(self.stack_newest.pop())

        if self.stack_oldest.is_empty():
            raise IndexError("Queue is empty")

    def display(self) -> None:
        """
        Display the elements in the queue from front to back.
        """
        if self.is_empty():
            print("Queue is empty")
        else:
            # Combine elements from both stacks, reversing the newest stack
            elements = list(self.stack_oldest.items) + list(reversed(self.stack_newest.items))
            print("Front ->", " <- ".join(map(str, elements)), "<- Back")


def interactive_queue_demo():
    """
    Provide an interactive demonstration of the QueueWithStacks implementation.
    Users can perform various queue operations and see the results.
    """
    q = QueueWithStacks()
    
    while True:
        # Display menu options
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
    interactive_queue_demo()