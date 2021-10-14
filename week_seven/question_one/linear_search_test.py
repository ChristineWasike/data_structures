import unittest
from week_seven.question_one.linear_search import *


class LinearSearchTest(unittest.TestCase):
    def test_when_array_is_empty(self):
        test_array = []
        item = 1
        self.assertEqual(linear_search(test_array, item), False)

    def test_when_item_is_none(self):
        test_array = [1, 2, 3, 4]
        item = None
        self.assertEqual(linear_search(test_array, item), False)

    def test_when_searching_for_string_in_int_array(self):
        test_array = [1, 2, 3, 4]
        item = "one"
        self.assertEqual(linear_search(test_array, item), False)

    def test_when_two_instances_of_the_item_exist(self):
        test_array = [1, 2, 3, 4, 1]
        item = 1
        self.assertEqual(linear_search(test_array, item), True)
