import unittest
from week_six.question_two.gdc import *


class GcdTest(unittest.TestCase):
    def test_calculate_gcd_of_two_numbers(self):
        self.assertEqual(calculate_gcd(252, 105), 21)

    def test_two_similar_numbers(self):
        self.assertEqual(calculate_gcd(54, 54), 54)

    def test_swap_smaller_larger_number(self):
        self.assertEqual(calculate_gcd(18, 45), 9)

    def test_negative_numbers(self):
        self.assertEqual(calculate_gcd(-6, 100), 2)

    def test_one_number_is_one(self):
        self.assertEqual(calculate_gcd(34, 1), 1)

    def test_at_least_one_number_is_zero(self):
        self.assertEqual(calculate_gcd(87, 0), "Cannot compute gcd of a pair of numbers when one of them is 0.")
