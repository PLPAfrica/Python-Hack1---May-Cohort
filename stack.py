import os
import pickle
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime

# Function to Load Data from File
def load_from_file(filename):
    if os.path.exists(filename):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except EOFError:
            print(f"File {filename} is empty. Initializing empty data.")
            return []
        except Exception as e:
            print(f"Error loading file {filename}: {e}")
            return []
    else:
        print(f"File {filename} not found. Initializing empty data.")
        return []

# Function to Save Data to File
def save_to_file(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
    print(f"Data saved to {filename}.")

# Function to Reverse the Stack
def reverse_stack(stack):
    return stack[::-1]

# Function to Reverse a Specific String
def reverse_specific_string(stack, string_to_reverse):
    for i in range(len(stack)):
        if stack[i] == string_to_reverse:
            stack[i] = stack[i][::-1]
            return True
    return False

# Function for Caesar Cipher Encryption
def caesar_cipher(s: str, shift: int) -> str:
    encrypted_string = ''
    for char in s:
        encrypted_string += chr((ord(char) + shift - 32) % 95 + 32)
    return encrypted_string

# Function to Display Menu
def display_menu():
    print("\nChoose an option:")
    print("1. Add element")
    print("2. Delete element")
    print("3. Reverse elements")
    print("4. Encrypt elements")
    print("5. Undo last operation")
    print("6. Redo last operation")
    print("7. Save stack to file")
    print("8. Load stack from file")
    print("9. Show stack statistics")
    print("10. Search and replace element")
    print("11. Reverse specific string")
    print("12. Save history to PDF")
    print("13. Load history from PDF")
    print("14. Delete specific history entry")
    print("15. Exit")

    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to Display Stack
def display_stack(stack):
    print("Current Stack:", stack)

# Function to Save History to PDF
def save_history_to_pdf(history, username, filename='history.pdf'):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y = height - 40  # Start from top of the page

    # Add title with username
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, y, f"{username}'s Report")
    y -= 40

    c.setFont("Helvetica", 12)
    c.drawString(30, y, "Stack Operation History:")
    y -= 20

    for idx, entry in enumerate(history):
        action, data = entry
        c.drawString(30, y, f"{idx + 1}. {action}: {data if data else ''}")
        y -= 20
        if y < 40:  # Check if we need a new page
            c.showPage()
            y = height - 40

    c.save()
    print(f"History saved to {filename}.")

# Function to Load History from PDF
def load_history_from_pdf(filename='history.pdf'):
    if os.path.exists(filename):
        print(f"History file {filename} exists.")
    else:
        print(f"History file {filename} not found.")
    return []  # Placeholder, as reading and parsing PDF is more complex

# Function to Draw Stack Visualization
def draw_stack(stack, filename='stack.pdf'):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y = height - 40  # Start from top of the page
    x = 2 * inch

    c.setFont("Helvetica", 12)
    c.drawString(30, y, "Stack Visualization:")
    y -= 20

    for idx, item in enumerate(stack):
        # Draw node
        c.circle(x, y, 0.2 * inch, fill=1)
        c.setFillColor('white')
        c.drawCentredString(x, y, str(item))
        c.setFillColor('black')
        y -= 0.5 * inch

        # Draw arrow to next node
        if idx < len(stack) - 1:
            x2, y2 = x, y + 0.5 * inch
            c.line(x, y, x, y2)
            c.line(x, y2, x - 0.2 * inch, y2 + 0.2 * inch)
            c.line(x, y2, x + 0.2 * inch, y2 + 0.2 * inch)

    c.save()
    print(f"Stack diagram saved to {filename}.")

def main():
    stack = []
    history = load_from_file('history.pkl')  # Ensure history file is loaded
    redo_stack = []
    user_authenticated = False

    # User Authentication
    while not user_authenticated:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "salim" and password == "1234":
            print("User authenticated successfully!")
            user_authenticated = True
        else:
            print("Invalid credentials. Try again.")

    while True:
        display_stack(stack)
        choice = display_menu()

        if choice == 1:
            try:
                num_elements = int(input("Enter the number of elements: "))
                for i in range(num_elements):
                    element = input(f"Enter element {i+1}: ")
                    stack.append(element)
                    history.append(('add', element))
                redo_stack.clear()
                draw_stack(stack)
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == 2:
            if stack:
                removed_element = stack.pop()
                history.append(('delete', removed_element))
                redo_stack.clear()
                print(f"Element '{removed_element}' deleted from the stack.")
                draw_stack(stack)
            else:
                print("The stack is empty. Nothing to delete.")
        
        elif choice == 3:
            if stack:
                stack = reverse_stack(stack)
                history.append(('reverse', None))
                redo_stack.clear()
                print("Stack reversed.")
                draw_stack(stack)
            else:
                print("The stack is empty. Nothing to reverse.")
        
        elif choice == 4:
            if stack:
                try:
                    shift = int(input("Enter shift value for encryption: "))
                    stack = [caesar_cipher(el, shift) for el in stack]
                    history.append(('encrypt', shift))
                    redo_stack.clear()
                    print("Stack encrypted.")
                    draw_stack(stack)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("The stack is empty. Nothing to encrypt.")
        
        elif choice == 5:
            if history:
                last_action, data = history.pop()
                if last_action == 'add':
                    stack.remove(data)
                elif last_action == 'delete':
                    stack.append(data)
                elif last_action == 'reverse':
                    stack = reverse_stack(stack)
                elif last_action == 'encrypt':
                    stack = [caesar_cipher(el, -data) for el in stack]
                redo_stack.append((last_action, data))
                print("Undid last operation.")
                draw_stack(stack)
            else:
                print("No operation to undo.")
        
        elif choice == 6:
            if redo_stack:
                last_action, data = redo_stack.pop()
                if last_action == 'add':
                    stack.append(data)
                elif last_action == 'delete':
                    stack.pop()
                elif last_action == 'reverse':
                    stack = reverse_stack(stack)
                elif last_action == 'encrypt':
                    stack = [caesar_cipher(el, data) for el in stack]
                history.append((last_action, data))
                print("Redid last operation.")
                draw_stack(stack)
            else:
                print("No operation to redo.")
        
        elif choice == 7:
            filename = input("Enter filename to save stack: ")
            save_to_file(filename, stack)
        
        elif choice == 8:
            filename = input("Enter filename to load stack: ")
            loaded_stack = load_from_file(filename)
            if loaded_stack is not None:
                stack = loaded_stack
        
        elif choice == 9:
            if stack:
                print(f"Number of elements: {len(stack)}")
                if all(el.isdigit() for el in stack):
                    numeric_stack = list(map(int, stack))
                    print(f"Maximum element: {max(numeric_stack)}")
                    print(f"Average value: {sum(numeric_stack) / len(numeric_stack)}")
                else:
                    print("Non-numeric elements found. Statistics are limited.")
            else:
                print("The stack is empty.")
        
        elif choice == 10:
            search_element = input("Enter element to search: ")
            if search_element in stack:
                replace_element = input("Enter element to replace with: ")
                stack = [replace_element if el == search_element else el for el in stack]
                print(f"Element '{search_element}' replaced with '{replace_element}'.")
                draw_stack(stack)
            else:
                print(f"Element '{search_element}' not found in the stack.")
        
        elif choice == 11:
            string_to_reverse = input("Enter the string to reverse in the stack: ")
            if reverse_specific_string(stack, string_to_reverse):
                history.append(('reverse_specific', string_to_reverse))
                redo_stack.clear()
                print(f"String '{string_to_reverse}' reversed in the stack.")
                draw_stack(stack)
            else:
                print(f"String '{string_to_reverse}' not found in the stack.")
        
        elif choice == 12:
            save_history_to_pdf(history, username)
        
        elif choice == 13:
            load_history_from_pdf()
        
        elif choice == 14:
            if history:
                print("History:")
                for idx, entry in enumerate(history):
                    print(f"{idx + 1}. {entry}")
                try:
                    entry_to_delete = int(input("Enter the number of the history entry to delete: "))
                    if 1 <= entry_to_delete <= len(history):
                        del history[entry_to_delete - 1]
                        print("History entry deleted.")
                        save_history_to_pdf(history, username)  # Save changes to PDF
                    else:
                        print("Invalid entry number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("No history available to delete.")
        
        elif choice == 15:
            print("Exiting the program. Goodbye!")
            save_history_to_pdf(history, username)
            save_to_file('history.pkl', history)  # Save history before exiting
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
