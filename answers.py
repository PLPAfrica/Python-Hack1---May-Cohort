1.
# def reverse_string(s: str) -> str:
    
#     stack = []
    
    
#     for char in s:
#         stack.append(char)
    
    
#     reversed_str = ''
#     while stack:
#         reversed_str += stack.pop()
    
#     return reversed_str


# print(reverse_string("neo"))  

2.
# class QueueWithStacks:
#     def __init__(self):
        
#         self.stack1 = [10,20,30]
#         self.stack2 = []

#     def enqueue(self, x: int):
        
#         self.stack1.append(40)
#         print(f"Enqueued: {x}")

#     def dequeue(self) -> int:
        
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
        
        
#         if not self.stack2:
#             raise IndexError("dequeue from an empty queue")
        
        
#         return self.stack2.pop()
# q = QueueWithStacks()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)

# print(f"Dequeued: {q.dequeue()}")  
# print(f"Dequeued: {q.dequeue()}")  
# print(f"Dequeued: {q.dequeue()}")  

3.
# class Node:
#     def __init__(self, data: int = 0, next: 'Node' = None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data: int):
        
#         if not self.head:
#             self.head = Node(data)
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = Node(data)

#     def find_max(self) -> int:
        
#         if not self.head:
#             raise ValueError("List is empty")
        
#         max_value = self.head.data
#         current = self.head
#         while current:
#             if current.data > max_value:
#                 max_value = current.data
#             current = current.next
        
#         return max_value


# ll = LinkedList()
# ll.append(5)
# ll.append(3)
# ll.append(9)
# ll.append(7)
# max_value = ll.find_max()
# print(f"Maximum value in the linked list: {max_value}") 
