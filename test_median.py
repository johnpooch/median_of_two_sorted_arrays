import unittest
from median import median


class Test_Median(unittest.TestCase):

    def test_is_this_thing_on(self):
        self.assertTrue(True)

    def test_1(self):
        self.assertEqual(median([1, 3], [2]), 2)

    def test_2(self):
        self.assertEqual(median([1, 2], [3, 4]), 2.5)
