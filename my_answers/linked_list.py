class Node:
    def __init__(self, product_id, name, price):
        
        self.product_id = product_id  # Store the product ID
        self.name = name  # Store the product name
        self.price = price  # Store the product price
        self.next = None  # Initialize the next pointer to None


class LinkedList:
    def __init__(self):
        #Initialize an empty linked list.#
        self.head = None  # The head of the linked list (first node)

    def append(self, product_id: int, name: str, price: float):
        #Add a new product to the end of the linked list.#
        new_node = Node(product_id, name, price)  # Create a new node with product details
        if not self.head:
            # If the list is empty, the new node becomes the head
            self.head = new_node
            return

        # Traverse to the last node in the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # Append the new node at the end of the list
        last_node.next = new_node

    def find_most_expensive(self):
        #Find and return the product with the highest price.#
        if not self.head:
            raise ValueError("The list is empty, no products to compare.")  # Handle the empty list case
        
        # Initialize the max_price_node to the head of the list
        max_price_node = self.head
        current_node = self.head.next  # Start checking from the second node

        while current_node:
            # If the current node's price is higher than max_price_node's price, update max_price_node
            if current_node.price > max_price_node.price:
                max_price_node = current_node
            current_node = current_node.next  # Move to the next node

        return max_price_node  # Return the node with the highest price


# Here is the example I used to demonstrate this. It fetches the most expensive item from a list.
if __name__ == "__main__":
    # Create a linked list to store products
    products = LinkedList()

    # Append products with IDs, names, and prices to the linked list
    products.append(101, "Laptop", 1200.99)  # This is the most expensive product in the list
    products.append(102, "Smartphone", 899.99)
    products.append(103, "Tablet", 499.99)
    products.append(104, "Monitor", 299.99)
    products.append(105, "Printer", 150.00)
    products.append(106, "Headphones", 199.99)
    products.append(107, "Webcam", 89.99)
    products.append(108, "External Hard Drive", 129.99)
    products.append(109, "Mouse", 29.99)
    products.append(110, "Keyboard", 49.99)

    # Finding the most expensive product in the linked list
    most_expensive = products.find_most_expensive()

    # Printing the name and price of the most expensive product
    print(f"The most expensive product is '{most_expensive.name}' with a price of ${most_expensive.price}")
