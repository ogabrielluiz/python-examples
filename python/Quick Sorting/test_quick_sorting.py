import unittest
from quick_sorting import quick_sorting


class TestQuickSorting(unittest.TestCase):
    def test_quick_sortingg(self):
        test_array = [1, 3, 2, 4, 5]
        sorted_array = quick_sorting(test_array)
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
