import unittest
from week_eight.question_one.TreeCreator import *


class TreeCreatorTest(unittest.TestCase):
    def test_that_a_simple_list_of_lists_is_a_tree(self):
        test_list = [1, [2, [4, 5]], [3, 6, 7]]
        self.assertEqual(tree_checker(test_list), "This is a tree")

    def test_list_with_no_item(self):
        test_list = []
        self.assertEqual(tree_checker(test_list), "This is not a tree because: it is empty")

    def test_list_with_list_first_element_type(self):
        test_list = [[1], [2]]
        self.assertEqual(tree_checker(test_list), "This is not a tree because: first element not an integer")

    def test_dictionary_as_a_tree(self):
        test_dictionary = {1: 50, 2: 10}
        self.assertEqual(tree_checker(test_dictionary), "This is not tree because: it is not a list")

    def test_simple_list_with_two_elements(self):
        test_list = [3, 4]
        self.assertEqual(tree_checker(test_list), "This is a tree")
