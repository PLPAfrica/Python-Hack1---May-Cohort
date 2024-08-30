class Node:
    def __init__(self, data):
        # initializing a new node
        self.data = data #storing the value in the node
        self.next = None #initializing the next pointer to none

class LinkedList:
    def __init__(self):
        # initializing the linked list with an empty head
        self.head = None

    def append(self, data):
        # creating a nwe node
        new_node = Node(data)

        # If head is None, set the new node as the head
        if not self.head:
            self.head= new_node
        else:
            # if there is something traverse to the end of the list
            current = self.head
            while current.next:
                current = current.next
                # Linking the last node to the last new node
            current.next = new_node

    def find_max(self) -> int:
        # checking if there is an error and if there is one, raise an error
        if not self.head:
            raise ValueError("The list is empty")
        
        # starting with the first node's data and as the maximum value
        max_value = self.head.data
        # Checking for the second node if any
        current = self.head.next

        # Traversing though the list till the end
        while current:
            # if the current node's data is greater than the max value, update max_value
            if current.data > max_value:
                max_value = current.data

            # MOving to the next node
            current = current.next

            # returning to the highest value we found
        return max_value
    

# Using it in an example
ll = LinkedList()  #creating a new linked list
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  #finging and printing the maximum valyue in the linked list
