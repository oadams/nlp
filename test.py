import unittest
from distance import min_edit_distance

class TestDistance(unittest.TestCase):

    def test_default_min_edit_distance(self):
        self.assertEqual(min_edit_distance("intention", "execution"), 5)
        self.assertEqual(min_edit_distance("kitten", "sitting"), 3)
        self.assertEqual(min_edit_distance("rosettacode", "raisethysword"), 8)
        self.assertEqual(min_edit_distance("saturday", "sunday"), 3)
        self.assertEqual(min_edit_distance("donkey", "horse"), 4)
        self.assertEqual(min_edit_distance("industry", "interest"), 6)

if __name__ == "__main__":
    unittest.main()
