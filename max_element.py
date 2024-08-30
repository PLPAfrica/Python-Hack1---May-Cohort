#Represents a single node in a linked list
class Node:
    #Initializes a new node with the given data.
    def __init__(self, data):
        self.data = data
        self.next = None

#Represents a singly linked list
class LinkedList:
    #Initializes an empty linked list
    def __init__(self):
        self.head = None

    #Appends a new node with the given data to the end of the list.
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    #Finds the maximum value in the linked list.
    def find_max(self):
        
        if not self.head:
            return None

        max_value = self.head.data
        current_node = self.head.next
        while current_node:
            if current_node.data > max_value:
                max_value = current_node.data
            current_node = current_node.next
        return max_value

#Main function to create a linked list and find the maximum element.
def main():
    linked_list = LinkedList()
    while True:
        data = input("Enter an element (or 'quit' to exit): ")
        if data.lower() == "quit":
            break
        linked_list.append(int(data))

    max_value = linked_list.find_max()
    if max_value is not None:
        print("Maximum value:", max_value)
    else:
        print("Linked list is empty.")

if __name__ == "__main__":
    main()