import unittest
from week_four.question_one.Stack import *


class StackTest(unittest.TestCase):
    # Check that a stack has been created
    def test_create_a_stack(self):
        test_array = [345, 567, 901, 234, 456]
        test_stack = Stack(test_array)
        self.assertEqual(str(test_stack), "[345, 567, 901, 234, 456]")

    # Check that the peek method works well ie returns the last item in the stack
    def test_peek_method(self):
        test_array = [54, 76, 21, 43, 65]
        test_stack = Stack(test_array)
        self.assertEqual(test_stack.peek(), 65)

    # Check that an element is added onto the stack as the last item.
    def test_push_method(self):
        test_array = ["One", "Two", "Three", "Four", "Five"]
        test_stack = Stack(test_array)
        self.assertEqual(test_stack.push("Six"), ["One", "Two", "Three", "Four", "Five", "Six"])

    # Check that the last item in the stack is removed.
    def test_pop_method(self):
        test_array = ["Deer", "Horse", "Zebra", "Donkey", "Buffalo"]
        test_stack = Stack(test_array)
        self.assertEqual(test_stack.pop(), ["Deer", "Horse", "Zebra", "Donkey"])
