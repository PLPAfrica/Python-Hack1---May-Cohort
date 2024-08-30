import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from max_element import LinkedList, Node

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_append_and_display(self):
        # Test appending to an empty list
        self.ll.append(5)
        self.assertEqual(self.ll.head.data, 5)
        
        # Test appending multiple elements
        self.ll.append(10)
        self.ll.append(15)
        
        # Capture the output of display() method
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.ll.display()
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "5 -> 10 -> 15")

    def test_find_max(self):
        # Test find_max on an empty list
        self.assertIsNone(self.ll.find_max())
        
        # Test find_max with one element
        self.ll.append(5)
        self.assertEqual(self.ll.find_max(), 5)
        
        # Test find_max with multiple elements
        self.ll.append(10)
        self.ll.append(3)
        self.assertEqual(self.ll.find_max(), 10)
        
        # Test find_max with negative numbers
        self.ll.append(-20)
        self.assertEqual(self.ll.find_max(), 10)

    def test_edge_cases(self):
        # Test appending None
        with self.assertRaises(TypeError):
            self.ll.append(None)
        
        # Test appending non-comparable types
        self.ll.append(5)
        with self.assertRaises(TypeError):
            self.ll.append("string")
        
        # Test with very large numbers
        self.ll.append(10**1000)
        self.assertEqual(self.ll.find_max(), 10**1000)

    def test_display_empty_list(self):
        # Capture the output of display() method for an empty list
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.ll.display()
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "Empty list")

if __name__ == '__main__':
    unittest.main()