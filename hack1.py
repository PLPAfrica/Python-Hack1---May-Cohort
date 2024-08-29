#reversing a string using a stack
# def reverse_string(s: str) -> str:
#     stack = []

#     #pushing all characters of the string onto the stack
#     for char in s:
#         stack.append(char)

#     #popping all characters from the stack to form the reversed string
#     reversed_str = ''
#     while stack:
#         reversed_str += stack.pop()

#     return reversed_str

# #test case
# print(reverse_string("Hello"))


#implementing a queue using two stacks
# class QueueWithStacks:
#     def __init__(self):
#         #two stacks for enqueue and dequeue operations
#         self.stack_in = []
#         self.stack_out = []

#     def enqueue(self, x: int):
#         #add an element to the end of stack_in
#         self.stack_in.append(x)

#     def dequeue(self) -> int:
#         #move all elements stack_in to stack_out if stack_out is empty
#         if not self.stack_out:
#             while self.stack_in:
#                 self.stack_out.append(self.stack_in.pop())
#         #pop and return the top element from stack_out if it's not empty
#         return self.stack_out.pop() if self.stack_out else None

# #test case
# q = QueueWithStacks()
# q.enqueue(12)
# q.enqueue(28)

# print(q.dequeue())
# print(q.dequeue())

#finding the maximum element in a list using a linked list
class Node:
    def __init__(self, data: int):
        #store the value of the node
        self.data = data
        #pointer to the next node in the linked list
        self.next = None

#to manage the linked list operations
class LinkedList:
    def __init__(self):
        self.head = None

    #append a new node 
    def append(self, data: int):
        new_node = Node(data)
        #if the linked list is empty then set the new node as the head
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    #findind the maximum element in the linked list
    def find_max(self) -> int:
        if not self.head:
            #return None if the list is empty
            return None
        
        max_value = self.head.data
        current = self.head.next

        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value


#test case
L_L = LinkedList()

L_L.append(10)
L_L.append(6)
L_L.append(28)
L_L.append(2)

print(L_L.find_max())
