import os
import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    
    def find_max(self):
        if not self.head:
            raise ValueError("The list is empty")
        max_value = self.head.data
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

    def draw_list(self):
        filename = self._generate_filename()
        
        for attempt in range(5):  # Retry mechanism
            try:
                self._create_pdf(filename)
                print(f"Linked list diagram saved to {filename}.")
                self._open_file(filename)
                break
            except PermissionError:
                print(f"Permission denied. Retrying in 1 second...")
                time.sleep(1)
            except Exception as e:
                print(f"An error occurred: {e}")
                break

    def display_list(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        print("Linked List elements:")
        while current:
            print(f" -> {current.data}", end="")
            current = current.next
        print()  # Newline for better readability

    def _generate_filename(self):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        return f'linkedlist_{timestamp}.pdf'

    def _create_pdf(self, filename):
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        x, y = 1 * inch, height - 2 * inch
        node_radius = 0.2 * inch

        c.setFont("Helvetica", 12)
        current = self.head
        while current:
            # Draw node
            c.circle(x, y, node_radius, fill=1)
            c.setFillColor('white')
            c.drawCentredString(x, y, str(current.data))
            c.setFillColor('black')
            
            # Draw arrow to next node
            if current.next:
                x2, y2 = x + 1.5 * node_radius, y
                c.line(x + node_radius, y, x2 - node_radius, y)
                c.line(x2 - node_radius, y, x2, y)
                c.line(x2, y, x2 - node_radius, y + 0.2 * node_radius)
                c.line(x2, y, x2 - node_radius, y - 0.2 * node_radius)
                x, y = x2, y
            current = current.next

        c.save()

    def _open_file(self, filename):
        try:
            if os.name == 'nt':  # For Windows
                subprocess.run(['code', filename], check=True)
            elif os.name == 'posix':  # For macOS/Linux
                subprocess.run(['code', filename], check=True)
            else:
                print("Unsupported OS. Please open the file manually.")
        except FileNotFoundError:
            # Fallback to default system application
            if os.name == 'nt':
                os.startfile(filename)
            else:
                subprocess.run(['xdg-open', filename])

def main():
    linked_list = LinkedList()

    while True:
        choice = input("Choose an option:\n1. Add element\n2. Find maximum element\n3. Display list\n4. Draw list\n5. Exit\n> ")

        if choice == '1':
            while True:
                element = input("Enter element to add (type 'done' to stop): ")
                if element.lower() == 'done':
                    break
                try:
                    element = int(element)
                    linked_list.append(element)
                except ValueError:
                    print("Please enter a valid integer.")
        
        elif choice == '2':
            try:
                max_value = linked_list.find_max()
                print(f"The maximum element in the list is: {max_value}")
            except ValueError as e:
                print(e)
        
        elif choice == '3':
            linked_list.display_list()
        
        elif choice == '4':
            linked_list.draw_list()
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
