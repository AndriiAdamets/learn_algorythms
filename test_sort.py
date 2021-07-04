import unittest
import sort


class TestSort(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(sort.bubble_sort([7, 10, 4, 6, 8, 1, 3, 2, 9, 5]), [
                         1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_smallest_item_index(self):
        self.assertEqual(sort.smallest_item_index([4, 7, -1, 8, 22]), 2)

    def test_selection_sort(self):
        self.assertEqual(sort.selection_sort([7, 10, 4, 6, 8, 1, 3, 2, 9, 5]), [
                         1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_quick_sort(self):
        self.assertEqual(sort.quick_sort([7, 10, 4, 6, 8, 1, 3, 2, 9, 5]), [
                         1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
