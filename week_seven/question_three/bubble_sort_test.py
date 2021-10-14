import unittest
from week_seven.question_three.bubble_sort import *


# Note: cannot have a list with mixed data types a comparison can not be
# drawn between an integer and string for instance.

class BubbleSortTest(unittest.TestCase):
    def test_sorting_a_list_in_descending_order(self):
        test_array = [5, 4, 3, 2, 1]
        self.assertEqual(bubble_sort(test_array), [1, 2, 3, 4, 5])

    def testing_an_empty_array(self):
        test_array = []
        self.assertEqual(bubble_sort(test_array), [])

    def test_array_with_repeated_integers(self):
        test_array = [9, 4, 10, 4, 7, 5, 9]
        self.assertEqual(bubble_sort(test_array), [4, 4, 5, 7, 9, 9, 10])
