class Node:
    def __init__(self, value: int):
        """
        Initializes a node with the given value and no next node.

        Parameters:
        value (int): The value to store in the node.
        """
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def append(self, value: int):
        """
        Appends a new node with the given value to the end of the list.

        Parameters:
        value (int): The value to add to the linked list.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Added {value} to the linked list.")
        self.display_list()

    def find_max(self) -> int:
        """
        Finds and returns the maximum value in the linked list.

        Returns:
        int: The maximum value in the linked list.

        Raises:
        ValueError: If the linked list is empty.
        """
        if self.head is None:
            raise ValueError("Cannot find max in an empty linked list.")

        max_value = self.head.value
        current = self.head.next

        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next

        return max_value

    def display_list(self):
        """
        Displays the current state of the linked list.
        """
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print("Current linked list: " +
              " -> ".join(values) if values else "Empty")


# Example usage:
if __name__ == "__main__":
    ll = LinkedList()

    while True:
        action = input(
            "Enter 'append' to add a value, 'find_max' to find the maximum value, or 'exit' to quit: ").strip().lower()

        if action == 'append':
            value = int(
                input("Enter the integer to add to the linked list: ").strip())
            ll.append(value)
        elif action == 'find_max':
            try:
                max_value = ll.find_max()
                print(f"The maximum value in the linked list is: {max_value}")
            except ValueError as e:
                print(e)
        elif action == 'exit':
            print("Exiting the program.")
            break
        else:
            print("Invalid action. Please enter 'append', 'find_max', or 'exit'.")
