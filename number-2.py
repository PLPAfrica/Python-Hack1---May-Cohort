# 2. Implement a Queue Using Two Stacks

class QueueWithStacks:
    def __init__(self):
        self.stack_1 = [] 
        self.stack_2 = [] 

    def enqueue(self, x: int):
        self.stack_1.append(x)

    def dequeue(self) -> int:
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())

        
        if self.stack_2:
            return self.stack_2.pop()
        return None  

#Example 
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  
print(q.dequeue())  
