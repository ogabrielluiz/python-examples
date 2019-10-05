import unittest
from selection_sorting import selection_sorting


class TestSelectioSorting(unittest.TestCase):
    def test_selectio_sortingg(self):
        test_array = [1, 3, 2, 4, 5]
        sorted_array = selection_sorting(test_array)
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
