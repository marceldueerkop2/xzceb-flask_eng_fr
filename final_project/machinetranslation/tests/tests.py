"""These are Unittests for the translator"""
import unittest
from machinetranslation import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    """Tests for English to French"""
    def test_1(self):
        self.assertEqual(english_to_french(None), 'Provide Text')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    """Tests for French to English"""
    def test_2(self):
        self.assertEqual(french_to_english(None), 'Provide Text')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


unittest.main()
