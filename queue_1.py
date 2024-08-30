class QueueWithStacks:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return "No item"
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)

    def size(self):
        return(self.queue)
    

q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)

q.display()

q.dequeue()

print(f"after dequeing the element")
print(q.dequeue())
print(q.dequeue())