from src.queue_with_stacks import QueueWithStacks

class QueueWithStacks:
    def __init__(self):
        """
        This class implements a queue using two stacks. The enqueue operation is performed on stack1,
        and the dequeue operation is performed on stack2. When stack2 is empty, elements are transferred
        from stack1 to stack2 to ensure the correct order of elements.
        """
        self.stack1 = []  # enqueue operations
        self.stack2 = []  # dequeue operations

    def enqueue(self, x: int):
        """
        Adds an element to the back of the queue.

        Parameters:
        x (int): The element to be added to the queue.
        """
        self.stack1.append(x)

    def dequeue(self) -> int:
        """
        Removes and returns the front element of the queue.

        Raises:
        IndexError: If both stacks are empty, indicating that the queue is empty.

        Returns:
        int: The element at the front of the queue.
        """
        if not self.stack1 and not self.stack2:
            raise IndexError("Dequeue from an empty queue")

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def __str__(self):
        """
        Returns a string representation of the queue's current state.
        """
        if not self.stack2:
            return str(self.stack1)
        return str(self.stack2[::-1] + self.stack1)


def test_queue_with_stacks():
    """
    This function tests the functionality of a Queue implemented using two Stacks.

    The QueueWithStacks class has two methods:
    - enqueue(value): Adds an element to the end of the queue.
    - dequeue(): Removes and returns the element at the front of the queue.

    Raises:
        IndexError: If the dequeue method is called on an empty queue.
    """
    q = QueueWithStacks()
    q.enqueue("Lesson1")
    q.enqueue("Lesson2")

    # Test first dequeue
    first_out = q.dequeue()
    print(f"Dequeued: {first_out} | Queue state: {q}")
    assert first_out == "Lesson1"

    # Test second and third dequeues
    q.enqueue("Lesson3")
    print(f"Queue after enqueueing 3-Lessons: {q}")

    second_out = q.dequeue()
    print(f"Dequeued: {second_out} | Queue state: {q}")
    assert second_out == "Lesson2"

    third_out = q.dequeue()
    print(f"Dequeued: {third_out} | Queue state: {q}")
    assert third_out == "Lesson3"

    # Test dequeue on an empty queue
    try:
        empty_queue = QueueWithStacks()
        empty_queue.dequeue()
        assert False, "Did not raise IndexError for empty queue"
    except IndexError:
        print("IndexError raised as expected for empty queue")
        assert True


if __name__ == "__main__":
    test_queue_with_stacks()
    print("All QueueWithStacks tests passed!")
