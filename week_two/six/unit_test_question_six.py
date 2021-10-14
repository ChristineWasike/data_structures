from week_two.six.question_six import *
import unittest


class TestWhiteSpaceRemover(unittest.TestCase):
    # Check that whitespace between two words has been removed
    def test_whitespace_removed_between_two_words(self):
        self.assertEqual(whitespace_remover("Poisonous     toad"), "Poisonous toad")

    # Check that single spacing even within 'words' is not removed
    def test_single_space_between_words_remains(self):
        self.assertEqual(whitespace_remover("a simple a b c   testing pha se"), "a simple a b c testing pha se")

    # Check that whitespace at the end of strings is removed
    def test_whitespace_removed_at_end_of_string(self):
        self.assertEqual(whitespace_remover("I am a string with whitespace at the end      "),
                         "I am a string with whitespace at the end")

    # Check that whitespace at the start of a string is removed
    def test_remove_whitespace_at_start_of_string(self):
        self.assertEqual(whitespace_remover("      There is so much space in front of me."),
                         "There is so much space in front of me.")

    # Check that whitespace between the characters has been removed as well
    def test_remove_whitespace_between_characters(self):
        self.assertEqual(whitespace_remover("!    !    .    ,  ...      ."), "! ! . , ... .")
