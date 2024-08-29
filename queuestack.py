class QueueWithStacks:
    """
    A queue implemented using two stacks. This approach ensures that 
    elements are dequeued in the order they were enqueued (FIFO).
    """
    
    def __init__(self):
        """Initialize two stacks used to manage the queue."""
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        """Add an element to the back of the queue.

        Args:
            x (int): The element to be added to the queue.
        """
        self.stack1.append(x)

    def dequeue(self) -> int:
        """Remove and return the front element of the queue.

        Returns:
            int: The front element of the queue.
            
        Raises:
            IndexError: If the queue is empty when attempting to dequeue.
        """
        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            raise IndexError("dequeue from empty queue")
        
        return self.stack2.pop()

    def is_empty(self) -> bool:
        """Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not (self.stack1 or self.stack2)

    def peek(self) -> int:
        """Get the front element of the queue without removing it.

        Returns:
            int: The front element of the queue.
            
        Raises:
            IndexError: If the queue is empty when attempting to peek.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            raise IndexError("peek from empty queue")
        
        return self.stack2[-1]

    def display(self) -> list:
        """Display the elements in the queue from front to back.

        Returns:
            list: A list of elements currently in the queue.
        """
        # Transfer elements from stack1 to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Return the elements in stack2
        return self.stack2[::-1] + self.stack1

if __name__ == "__main__":
    q = QueueWithStacks()

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Display queue")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            try:
                value = int(input("Enter an integer to enqueue: "))
                q.enqueue(value)
                print(f"Enqueued {value}")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        elif choice == '2':
            try:
                print(f"Dequeued {q.dequeue()}")
            except IndexError as e:
                print(f"Error: {e}")

        elif choice == '3':
            try:
                print(f"Front element: {q.peek()}")
            except IndexError as e:
                print(f"Error: {e}")

        elif choice == '4':
            print("Queue is empty" if q.is_empty() else "Queue is not empty")

        elif choice == '5':
            print("Current queue contents:", q.display())

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")