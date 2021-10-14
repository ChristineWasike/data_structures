from week_two.eight.question_eight import *
import unittest


class TestListInLists(unittest.TestCase):
    # Check lists in lists with no duplicate elements nad all of the same data type
    def test_list_in_list_no_duplicate_elements(self):
        first_list = ["a", "b", "c"]
        second_list = ["d", "e", "f", "g"]
        third_list = ["h", "i", "j", "k", "l"]
        self.assertEqual(list_function(first_list, second_list, third_list),
                         ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])
