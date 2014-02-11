import unittest
from distance import min_edit_distance
from distance import min_edit_distance_align
from distance import cluster_alignment_errors
from wer import word_error_rate

class TestDistance(unittest.TestCase):

    def test_default_min_edit_distance(self):
        self.assertEqual(min_edit_distance("intention", "execution"), 5)
        self.assertEqual(min_edit_distance("kitten", "sitting"), 3)
        self.assertEqual(min_edit_distance("rosettacode", "raisethysword"), 8)
        self.assertEqual(min_edit_distance("saturday", "sunday"), 3)
        self.assertEqual(min_edit_distance("donkey", "horse"), 4)
        self.assertEqual(min_edit_distance("industry", "interest"), 6)

    def test_min_edit_distance(self):
        self.assertEqual(min_edit_distance("intention", "execution",
                sub_cost=lambda x, y: 0 if x == y else 2), 8)

    def test_default_min_edit_distance_align(self):
        self.assertEqual(
                min_edit_distance_align("sub", "sube"),
                [("s", "s"), ("u", "u"), ("b", "b"), ("*", "e")])
        self.assertEqual(
                min_edit_distance_align("horse", "ros"),
                [("h", "r"),("o", "o"),("r", "*"),("s", "s"),("e", "*")])
        self.assertEqual(
                min_edit_distance_align("kitten", "sitting"),
                [("k", "s"),("i", "i"),("t", "t"),("t", "t"),("e", "i"),("n",
                "n"), ("*", "g")])
        self.assertEqual(
                min_edit_distance_align("papes", "papers"),
                [("p","p"),("a","a"),("p","p"),("e","e"),("*","r"),("s","s")])
        self.assertEqual(
                min_edit_distance_align("saturday", "sunday"),
                [("s","s"),("a","*"),("t","*"),("u","u"),("r","n"),("d","d"),("a","a"),("y","y")])

    def test_cluster_alignment_errors(self):
        self.assertEqual(
                cluster_alignment_errors(min_edit_distance_align("saturday", "slnday")),
                [("s","s"),(["a","t","u","r"],["l","n"]),("d","d"),("a","a"),("y","y")])

class TestWER(unittest.TestCase):

    def test_word_error_rate(self):
        result = word_error_rate("i um the phone is i left the portable phone\
                upstairs last night".split(),
                "i got it to the fullest i love to portable form of\
                stores last night".split())
        self.assertEqual("{0:.1f}".format(result), "76.9")

if __name__ == "__main__":
    unittest.main()
