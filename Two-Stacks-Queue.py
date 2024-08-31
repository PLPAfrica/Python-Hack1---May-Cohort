class QueueWithStacks:
    def __init__(self):
        """
        Initializes two stacks to simulate queue operations.
        """
        self.stack1 = []  # Stack for enqueue operations
        self.stack2 = []  # Stack for dequeue operations

    def enqueue(self, x: int):
        """
        Adds an element to the end of the queue.

        Parameters:
        x (int): The element to be added to the queue.
        """
        self.stack1.append(x)
        print(f"Added {x} to the queue.")
        self.display_queue()

    def dequeue(self) -> int:
        """
        Removes and returns the element from the front of the queue.

        Returns:
        int: The front element of the queue.

        Raises:
        IndexError: If the queue is empty.
        """
        if not self.stack2:  # If stack2 is empty, transfer elements from stack1
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:  # If stack2 is still empty, the queue is empty
            raise IndexError("Cannot dequeue from an empty queue.")

        removed_element = self.stack2.pop()
        print(f"Removed {removed_element} from the queue.")
        self.display_queue()
        return removed_element

    def display_queue(self):
        """
        Displays the current state of the queue.
        """
        # To display the queue, we need to transfer elements from stack1 to stack2 if stack2 is empty
        temp_stack1 = list(self.stack1)
        temp_stack2 = list(self.stack2)

        # Transfer elements from stack1 to a temporary stack2
        while temp_stack1:
            temp_stack2.append(temp_stack1.pop())

        # Print the queue from the front to the back
        print("Current queue:", end=" ")
        if temp_stack2:
            print(" <- ".join(map(str, temp_stack2)))
        else:
            print("Empty")


# Example usage:
if __name__ == "__main__":
    q = QueueWithStacks()

    while True:
        action = input(
            "Enter 'enqueue' to add an element, 'dequeue' to remove an element, or 'exit' to quit: ").strip().lower()

        if action == 'enqueue':
            element = int(
                input("Enter the integer to add to the queue: ").strip())
            q.enqueue(element)
        elif action == 'dequeue':
            try:
                q.dequeue()
            except IndexError as e:
                print(e)
        elif action == 'exit':
            print("Exiting the program.")
            break
        else:
            print("Invalid action. Please enter 'enqueue', 'dequeue', or 'exit'.")
