from week_three.question_four.AssociativeArrayClass import *
import unittest


class AssociativeArrayTest(unittest.TestCase):
    def test_create_an_associative_array(self):
        my_dictionary = AssociativeArrayClass({1: "3", 2: "6", 3: "9"})
        self.assertEqual(my_dictionary.__str__(), "{1: '3', 2: '6', 3: '9'}")

    def test_remove_from_associative_array(self):
        my_dictionary = AssociativeArrayClass({1: "3", 2: "6", 3: "9"})
        self.assertEqual(my_dictionary.remove(2), {1: '3', 3: '9'})
