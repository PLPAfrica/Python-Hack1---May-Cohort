class Node:
    def __init__(self, data):
        self.data = data  # Store the node's data
        self.next = None  # Initialize the next pointer to None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty list with no head node

    def append(self, data):
        """
        Append a new node with the given data to the end of the linked list.
        
        Args:
            data: The data to be stored in the new node.
        
        Time Complexity: O(n) where n is the number of nodes in the list
        Space Complexity: O(1)
        """
        new_node = Node(data)  # Create a new node with the given data
        
        if not self.head:
            self.head = new_node  # If the list is empty, set the new node as the head
            return
        
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node  # Set the last node's next pointer to the new node

    def find_max(self):
        """
        Find and return the maximum element in the linked list.
        
        Returns:
            The maximum element in the list, or None if the list is empty.
        
        Time Complexity: O(n) where n is the number of nodes in the list
        Space Complexity: O(1)
        """
        if not self.head:
            return None  # Return None for an empty list
        
        max_value = self.head.data  # Initialize max_value with the first node's data
        current = self.head.next
        
        # Traverse the list, updating max_value when a larger element is found
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value

    def display(self):
        """
        Display all elements in the linked list.
        
        Time Complexity: O(n) where n is the number of nodes in the list
        Space Complexity: O(n) due to the list used to store elements for display
        """
        elements = []
        current = self.head
        
        # Traverse the list, collecting all elements
        while current:
            elements.append(str(current.data))
            current = current.next
        
        # Print the elements as a string, or "Empty list" if there are no elements
        print(" -> ".join(elements) if elements else "Empty list")

def interactive_linked_list():
    """
    Provides an interactive interface for users to manipulate a linked list
    and demonstrate its functionality.
    """
    ll = LinkedList()  # Create a new LinkedList instance
    
    while True:
        # Display the menu options
        print("\nLinked List Operations:")
        print("1. Append element")
        print("2. Find maximum")
        print("3. Display list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            try:
                data = int(input("Enter the element to append: "))
                ll.append(data)
                print(f"Appended {data} to the list.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == '2':
            max_value = ll.find_max()
            if max_value is not None:
                print(f"Maximum element: {max_value}")
            else:
                print("The list is empty.")
        elif choice == '3':
            print("Current list:")
            ll.display()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    interactive_linked_list()  # Start the interactive linked list program