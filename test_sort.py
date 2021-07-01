import unittest
import sort


class TestSort(unittest.TestCase):
    def test_smallest_item_index(self):
        self.assertEqual(sort.smallest_item_index([4, 7, -1, 8, 22]), 2)

    def test_selection_sort(self):
        self.assertEqual(sort.selection_sort([2, 4, 1, 5, 3]), [1, 2, 3, 4, 5])
