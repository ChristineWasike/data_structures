import unittest
from week_seven.question_two.special_sort import *


class SpecialSortTest(unittest.TestCase):
    def test_when_values_are_all_different(self):
        test_dictionary = {1: 100, 2: 200, 3: 300}
        self.assertEqual(special_sort(test_dictionary), {1: 100, 2: 200, 3: 300})

    def test_when_there_are_duplicate_values(self):
        test_dictionary = {8: 50, 6: 38, 2: 20, 4: 38, 9: 10, 10: 20}
        self.assertEqual(special_sort(test_dictionary), {9: 10, 2: 20, 10: 20, 4: 38, 6: 38, 8: 50})

    def test_when_values_contains_a_zero_(self):
        test_dictionary = {4: 0, 0: 20, 8: 40, 6: 50, 3: 68}
        self.assertEqual(special_sort(test_dictionary), {4: 0, 0: 20, 8: 40, 6: 50, 3: 68})
