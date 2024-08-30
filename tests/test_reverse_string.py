# test_stack_reverse.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from  reverse_string import reverse_string

class TestReverseString(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string("racecar"), "racecar")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertEqual(reverse_string("!@#$%^&*()"), ")(*&^%$#@!")

    def test_error_handling(self):
        with self.assertRaises(ValueError):
            reverse_string(12345)

if __name__ == "__main__":
    unittest.main()