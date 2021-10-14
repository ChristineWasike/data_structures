import unittest
import numpy as np

from week_six.question_four.determinant import *


class DeterminantTest(unittest.TestCase):
    def test_determinant_2x2_matrix(self):
        two_by_tow_matrix = [[5, 4], [2, 4]]
        self.assertEqual(calculate_determinant(two_by_tow_matrix), round(np.linalg.det(two_by_tow_matrix)))

    def test_determinant_3x3_matrix(self):
        three_by_three_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(calculate_determinant(three_by_three_matrix), round(np.linalg.det(three_by_three_matrix)))

    def test_random(self):
        pass
