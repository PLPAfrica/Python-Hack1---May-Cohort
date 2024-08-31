import os
import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime
import time

class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Add element to stack1
        self.stack1.append(x)
        print(f"Element {x} added to the queue.")
        self.display_queue()
        self.draw_queue()

    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Dequeue from an empty queue")
        return self.stack2.pop()

    def display_queue(self):
        # Combine elements from both stacks to show the current queue
        combined_queue = list(self.stack2[::-1]) + self.stack1
        print(f"Current Queue: {combined_queue}")

    def sort_queue(self, order='asc'):
        if self.stack2:
            combined_queue = list(self.stack2[::-1]) + self.stack1
        else:
            combined_queue = self.stack1
        sorted_queue = sorted(combined_queue, reverse=(order == 'desc'))
        self.stack1 = sorted_queue
        self.stack2 = []
        print(f"Queue sorted in {order}ending order.")
        self.display_queue()

    def draw_queue(self):
        filename = self._generate_filename()
        self._create_pdf(filename)
        print(f"Queue diagram saved to {filename}.")
        self._open_file(filename)

    def _generate_filename(self):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        return f'queue_{timestamp}.pdf'

    def _create_pdf(self, filename):
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        x, y = 1 * inch, height - 2 * inch
        node_radius = 0.2 * inch

        c.setFont("Helvetica", 12)
        combined_queue = list(self.stack2[::-1]) + self.stack1
        if combined_queue:
            for index, item in enumerate(combined_queue):
                # Draw node
                c.circle(x, y, node_radius, fill=1)
                c.setFillColor('white')
                c.drawCentredString(x, y, str(item))
                c.setFillColor('black')
                
                # Draw arrow to next node
                if index < len(combined_queue) - 1:
                    x2, y2 = x + 1.5 * node_radius, y
                    c.line(x + node_radius, y, x2 - node_radius, y)
                    c.line(x2 - node_radius, y, x2, y)
                    c.line(x2, y, x2 - node_radius, y + 0.2 * node_radius)
                    c.line(x2, y, x2 - node_radius, y - 0.2 * node_radius)
                    x, y = x2, y
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

def display_menu():
    print("\nChoose an option:")
    print("1. Add element to the queue")
    print("2. Remove element from the queue")
    print("3. Sort queue (asc/desc)")
    print("4. Display queue")
    print("5. Exit")

    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    queue = QueueWithStacks()

    while True:
        choice = display_menu()

        if choice == 1:
            while True:
                element = input("Enter element to add (type 'done' to stop): ")
                if element.lower() == 'done':
                    break
                try:
                    queue.enqueue(int(element))
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        
        elif choice == 2:
            try:
                removed_element = queue.dequeue()
                print(f"Element {removed_element} removed from the queue.")
            except IndexError as e:
                print(e)
        
        elif choice == 3:
            order = input("Enter sort order (asc/desc): ").strip().lower()
            if order in ['asc', 'desc']:
                queue.sort_queue(order)
            else:
                print("Invalid order. Please enter 'asc' or 'desc'.")
        
        elif choice == 4:
            queue.display_queue()
        
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
