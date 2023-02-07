from unittest import TestCase

from is_sorted import is_sorted


class Test(TestCase):
    def test_ascending_values(self):
        self.assertTrue(is_sorted([1, 2, 3]))

    def test_descending_values(self):
        self.assertFalse(is_sorted([3, 2, 1]))

    def test_empty_list(self):
        self.assertFalse(is_sorted([]))

    def test_size_1_list(self):
        self.assertTrue(is_sorted([1]))

    def test_same_values(self):
        self.assertTrue([0, 0, 0])