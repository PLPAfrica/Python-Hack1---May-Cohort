#implementing a queue using two stacks

class QueueWithStacks:
    def __init__(self):
        # Create stack one for enqueue
        self.stack1 = []

        # Create stack two for dequeue
        self.stack2 = []

    def enqueue(self, item):
        # Push the item onto stack1
        self.stack1.append(item)
        print(f'Enqueued {item}')

    def dequeue(self):
        # If both stacks are empty, the queue is empty
        if not self.stack1 and not self.stack2:
            print(f'Queue is empty!')
            return None

        # If stack2 is empty, move the elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Pop and return the element from stack2
        return self.stack2.pop()

#examples
queue = QueueWithStacks()
queue.enqueue(3)
queue.enqueue('Star') 
queue.enqueue('General')
print(f'Dequeued: {queue.dequeue()}')  # prints out 3 
print(f'Dequeued: {queue.dequeue()}') #prints out star
queue.enqueue('Position')
print(f'Dequeued: {queue.dequeue()}')  # prints out General
print(f'Dequeued: {queue.dequeue()}')  # prints out Position



