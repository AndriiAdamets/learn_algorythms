import unittest
import search


class TestSearch(unittest.TestCase):
    def test_binary(self):
        self.assertEqual(search.binary([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(search.binary([1, 2, 3, 4, 5], 6), -1)
