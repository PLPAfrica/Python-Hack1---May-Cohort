class LinkedList:
    def __init__(self):
        #Initialize an empty linked list
        self.head = None
        
    #create a new node in the linked list
    #Store the node in value and reference to the next node
    def create_node(self, value, next_node = None):
        return {'value':value, 'next':next_node}

    #function to append a new value to the end of the linked list
    def append(self, value):
        #if the list is empty, create the first node
        if self.head is None:
            self.head = self.create_node(value)
            return
        
        #Traverse to the end of the list
        current_node = self.head
        while current_node['next'] is not None:
            current_node = current_node['next']
        
        #Add the new node at the end
        current_node['next'] = self.create_node(value)
    
    #function to find max value in linked list
    def find_max(self) -> int:
        if self.head is None:
            raise ValueError("The list is empty, cannot find the maximum value.")
        
        #Initialize the maximum value with the value of the first node
        max_value = self.head['value']
        
        #Traverse list to find max value
        current_node = self.head
        while current_node is not None:
            if current_node['value'] > max_value:
                max_value = current_node['value']
            current_node = current_node['next']
            
        return max_value
    
#test the linkedlist class
if __name__ == "__main__":
    ll = LinkedList()
    
    while True:
        user_input = input("Enter numbers to add to the linked list. Type 'done' when finished: ")
        if user_input.lower() == 'done':
            break
        
        try:
            number = int(user_input)
            ll.append(number)
        except ValueError:
            print("Please enter a valid number.")
        
    #Find and print the max value
    if ll.head is not None:
        print(f"The maximum value in the linked list is: {ll.find_max()}")
    else:
        print("The linked list is empty, cannot find the maximum value.")