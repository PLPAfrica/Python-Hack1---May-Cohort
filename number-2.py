# 2. Implement a Queue Using Two Stacks

class QueueWithStacks:
    def __init__(self):
        self.stack1 = [] 
        self.stack2 = [] 

    def enqueue(self, x: int):
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        
        if self.stack2:
            return self.stack2.pop()
        return None  

#Example 
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  
print(q.dequeue())  
