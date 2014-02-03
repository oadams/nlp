import unittest
from distance import min_edit_distance
from wer import word_error_rate

class TestDistance(unittest.TestCase):

    def test_default_min_edit_distance(self):
        self.assertEqual(min_edit_distance("intention", "execution"), 5)
        self.assertEqual(min_edit_distance("kitten", "sitting"), 3)
        self.assertEqual(min_edit_distance("rosettacode", "raisethysword"), 8)
        self.assertEqual(min_edit_distance("saturday", "sunday"), 3)
        self.assertEqual(min_edit_distance("donkey", "horse"), 4)
        self.assertEqual(min_edit_distance("industry", "interest"), 6)

class TestWER(unittest.TestCase):

    def test_word_error_rate(self):
        result = word_error_rate("i um the phone is i left the portable phone\
                upstairs last night".split(),
                "i got it to the fullest i love to portable form of\
                stores last night".split())
        self.assertEqual("{0:.1f}".format(result), "76.9")

if __name__ == "__main__":
    unittest.main()