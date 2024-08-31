class Queuewithstacks:
    def __init__ (self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, x):
        self.stack1.append(x)
    def dequeue(self):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        dequeue_result = self.stack2.pop()
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return dequeue_result
        
q = Queuewithstacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.dequeue())