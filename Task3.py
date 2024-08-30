class Node:

    #a class used to represent a Node in a singly linked list.

    def __init__(self, data):
        self.data = data
        self.next = None

# a class used to represent a singly linked list

class LinkedList:


    def __init__(self):

        #initiate an empty linked list with the head set to none
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def find_max(self):
        if not self.head:
             # If the list is empty, return None
            return None 

        # Initialize max_value with the data of the head node
        max_value = self.head.data
        current = self.head.next

        # Traverse the list to find the maximum value

        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value

# create a linked list example append some values

linked_list = LinkedList()
linked_list.append(23)
linked_list.append(56)
linked_list.append(29)
linked_list.append(87)
linked_list.append(11)

max_value = linked_list.find_max()
print(f"The maximum value in the linked list is: {max_value}")
