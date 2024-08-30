class Item:
    def __init__(self, name, quantity):
        self.name = name        # Name of the item
        self.quantity = quantity  # Quantity of the item
        self.next = None       # Pointer to the next item, initially None

class Inventory:
    def __init__(self):
        self.head = None  # The start of the inventory list, initially empty

    def add_item(self, name, quantity):
        new_item = Item(name, quantity)  # Create a new item with the given name and quantity
        if self.head is None:
            self.head = new_item  # If the list is empty, the new item is the head
        else:
            current = self.head
            while current.next:  # Move to the end of the list
                current = current.next
            current.next = new_item  # Add new item at the end

    def find_max_quantity(self):
        if self.head is None:
            raise ValueError("The inventory is empty.")  # Handle empty list case
        
        max_item = self.head  # Start with the first item as the item with the maximum quantity
        current = self.head
        while current:
            if current.quantity > max_item.quantity:
                max_item = current  # Update max_item if the current item's quantity is larger
            current = current.next  # Move to the next item
        
        return max_item.name, max_item.quantity  # Return the name and quantity of the item with the highest quantity

# Print the inventory item with the highest quantity
inventory = Inventory()
inventory.add_item("Apples", 50)
inventory.add_item("Bananas", 75)
inventory.add_item("Oranges", 30)
inventory.add_item("Pears", 60)

item_name, item_quantity = inventory.find_max_quantity()
print(f"The item with the highest quantity is '{item_name}' with a quantity of {item_quantity}.")
