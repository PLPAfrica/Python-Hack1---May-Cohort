from QueueWithStacks import QueueWithStacks
from reverse_string import reverse_string
from max_element import LinkedList, Node

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
        print("7. Return to Main Menu")
        
        choice = input("Enter your choice (1-7): ")
        
        try:
            if choice == '1':
                value = input("Enter value to enqueue: ")
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
                print("Returning to main menu.")
                break
            else:
                print("Invalid choice. Please try again.")
        except IndexError as e:
            print(f"Error: {e}")

def interactive_string_reversal():
    print("Welcome to the String Reversal Program!")
    print("Enter 'quit' to return to the main menu.")

    while True:
        user_input = input("\nEnter a string to reverse: ")
        
        if user_input.lower() == 'quit':
            print("Returning to main menu.")
            break

        try:
            result = reverse_string(user_input)
            print(f"Original: {user_input}")
            print(f"Reversed: {result}")
            print(f"Is palindrome: {result == user_input}")
        except ValueError as e:
            print(f"Error: {e}")

def interactive_linked_list():
    ll = LinkedList()
    
    while True:
        print("\nLinked List Operations:")
        print("1. Append element")
        print("2. Find maximum")
        print("3. Display list")
        print("4. Return to Main Menu")
        
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
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Queue with Stacks")
        print("2. String Reversal")
        print("3. Linked List with Max Element")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            interactive_queue_demo()
        elif choice == '2':
            interactive_string_reversal()
        elif choice == '3':
            interactive_linked_list()
        elif choice == '4':
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()