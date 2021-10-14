import unittest

from week_nine.question_one.question_one import *


class CheckMinHeapTest(unittest.TestCase):
    def test_empty_list(self):
        test_list = []
        self.assertEqual(min_heap_check(test_list, 0, len(test_list) - 1), True)

    def test_list_with_single_item(self):
        test_list = [4]
        self.assertEqual(min_heap_check(test_list, 0, len(test_list) - 1), True)

    # TODO Revisit
    def test_unordered_list_(self):
        test_list = [8, 3, 2, 6, 7, 1]
        self.assertEqual(min_heap_check(test_list, 0, len(test_list) - 1), True)

    def test_max_heap_list(self):
        test_list = [90, 15, 10, 7, 12, 2, 7, 3]
        self.assertEqual(min_heap_check(test_list, 0, len(test_list) - 1), False)

    def test_reverse_max_heap(self):
        test_list = [3, 7, 2, 12, 7, 10, 15, 90]
        self.assertEqual(min_heap_check(test_list, 0, len(test_list) - 1), False)
