from week_three.question_one.ArrayClass import *
import unittest


class TestArrayClass(unittest.TestCase):
    # Check that an integer array has been initialised
    def test_array_initialized(self):
        test_array = ArrayClass([2, 4, 7])
        self.assertEqual(test_array.__str__(), "[2, 4, 7]")

    # Check length of array
    def test_array_length(self):
        test_array = ArrayClass([5, 2, 8, 3])
        self.assertEqual(test_array.array_length(), 4)

    # Check that the get element method works
    def test_array_get_element(self):
        test_array = ArrayClass([9, 6, 8, 3])
        self.assertEqual(test_array.get_element(2), 8)

    # Check that the set element method works when changing value in existing index
    def test_array_set_element(self):
        test_array = ArrayClass([8, 9, 6, 1])
        self.assertEqual(test_array.set_element(16, 3), 16)

    # Check that the array is of fixed size
    def test_array_fixed_array(self):
        test_array = ArrayClass([3, 5, 7, 9, 13])
        self.assertRaises(IndexError, test_array.set_element(18, 5))
