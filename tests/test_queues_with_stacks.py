import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from QueueWithStacks import Stack, QueueWithStacks

class TestQueueWithStacks(unittest.TestCase):
    def setUp(self):
        self.q = QueueWithStacks()

    def test_enqueue_dequeue(self):
        # Test enqueue and dequeue operations
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        
        self.assertEqual(self.q.dequeue(), 1)
        self.assertEqual(self.q.dequeue(), 2)
        self.assertEqual(self.q.dequeue(), 3)
        
        # Test dequeue on empty queue
        with self.assertRaises(IndexError):
            self.q.dequeue()

    def test_peek(self):
        # Test peek on empty queue
        with self.assertRaises(IndexError):
            self.q.peek()
        
        # Test peek after enqueue
        self.q.enqueue(5)
        self.assertEqual(self.q.peek(), 5)
        
        # Ensure peek doesn't remove the element
        self.assertEqual(self.q.peek(), 5)

    def test_is_empty_and_size(self):
        # Test on empty queue
        self.assertTrue(self.q.is_empty())
        self.assertEqual(self.q.size(), 0)
        
        # Test after enqueue
        self.q.enqueue(1)
        self.assertFalse(self.q.is_empty())
        self.assertEqual(self.q.size(), 1)
        
        # Test after dequeue
        self.q.dequeue()
        self.assertTrue(self.q.is_empty())
        self.assertEqual(self.q.size(), 0)

    def test_display(self):
        # Test display on empty queue
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.q.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Queue is empty")
        
        # Test display with elements
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.q.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Front -> 1 <- 2 <- 3 <- Back")

    def test_edge_cases(self):
        # Test with large number of elements
        for i in range(10000):
            self.q.enqueue(i)
        
        self.assertEqual(self.q.size(), 10000)
        self.assertEqual(self.q.dequeue(), 0)
        
        # Test with different data types
        self.q.enqueue("string")
        self.q.enqueue(3.14)
        self.q.enqueue([1, 2, 3])
        
        self.assertEqual(self.q.dequeue(), "string")
        self.assertEqual(self.q.dequeue(), 3.14)
        self.assertEqual(self.q.dequeue(), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()