# Task 1
def reverse_string(s: str) -> str:
    stack = []
    
    for char in s:
        stack.append(char)
    
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str


string = "hello world!"
reversed_string = reverse_string(string)
print(reversed_string)


#Task 2 
class StackQueue:
    def __init__(self):
        
        self.stack_in = []
        self.stack_out = []
    
    def enqueue(self, x: int):
        
        self.stack_in.append(x)
    
    def dequeue(self) -> int:
        
        if not self.stack_out:
                self.stack_out.append(self.stack_in.pop())
        
       
        if not self.stack_out:
            raise IndexError("Dequeue from an empty queue")
        
       
        return self.stack_out.pop()


queue = StackQueue()
queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)

print(queue.dequeue())  
print(queue.dequeue())  

queue.enqueue(400)
print(queue.dequeue())  
print(queue.dequeue()) 



#Task 3
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def append(self, data):
        """Method to add a new node to the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self):
        """Method to find the maximum element in the linked list."""
        if self.head is None:
            raise Exception("The linked list is empty.")

        max_value = self.head.data
        current = self.head.next

        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value



if __name__ == "__main__":
    linked_list = LinkedList()

    
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(15)
    linked_list.append(30)

    
    max_element = linked_list.find_max()
    print("The maximum element in the list is:", max_element)



