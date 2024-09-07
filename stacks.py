# Define the class to be tested
class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("dequeue from empty queue")
        return self.stack2.pop()

# Define test functions
def test_queue_with_stacks():
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    print("test_queue_with_stacks passed")



#Run the test
if __name__=="__main__":
    test_queue_with_stacks()
    print("queue_with stack test is passed!")