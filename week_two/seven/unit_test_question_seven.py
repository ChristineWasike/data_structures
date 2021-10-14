from week_two.seven.question_seven import *
import unittest


class TestCharacterOccurrence(unittest.TestCase):
    # Check the occurrence of characters in a simple string with no repeated letters
    def test_character_occurrence_in_simple_string(self):
        self.assertEqual(char_dictionary_function("simple"), {'s': 1, 'i': 1, 'm': 1, 'p': 1, 'l': 1, 'e': 1})

    # Check the occurrence of characters in a string with several repeated characters
    def test_character_occurrence_in_string_with_repeated_letters(self):
        self.assertEqual(char_dictionary_function("bookkeeper"), {'b': 1, 'o': 2, 'k': 2, 'e': 3, 'p': 1, 'r': 1})

    # Check character occurrence in a string containing special characters
    def test_character_occurrence_in_string_with_special_characters(self):
        self.assertEqual(char_dictionary_function("&ab#)&#"), {'&': 2, 'a': 1, 'b': 1, '#': 2, ')': 1})

    # Check character occurrence in a string with both upper and lowercase letters
    def test_character_occurrence_in_string_with_upper_and_lower_case_letters(self):
        self.assertEqual(char_dictionary_function("ABCabc"), {'A': 1, 'B': 1, 'C': 1, 'a': 1, 'b': 1, 'c': 1})

    # Check character occurrence in a string that also contains integers
    def test_character_occurrence_in_string_with_integers(self):
        self.assertEqual(char_dictionary_function("Seventytwo7272"),
                         {'S': 1, 'e': 2, 'v': 1, 'n': 1, 't': 2, 'y': 1, 'w': 1, 'o': 1, '7': 2, '2': 2})

    # Check character occurrence of a sentence string
    def test_character_occurrence_in_a_sentence(self):
        self.assertEqual(char_dictionary_function("I am a sentence with whitespaces    "),
                         {'I': 1, ' ': 9, 'a': 3, 'm': 1, 's': 3, 'e': 5, 'n': 2, 't': 3, 'c': 2, 'w': 2, 'i': 2,
                          'h': 2, 'p': 1})  # Spaces are ignored
