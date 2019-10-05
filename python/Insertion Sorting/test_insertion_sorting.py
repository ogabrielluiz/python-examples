import unittest
from insertion_sorting import insertion_sorting


class TestInsertionSorting(unittest.TestCase):
    def test_insertion_sorting(self):
        test_array = [1, 3, 2, 4, 5]
        sorted_array = insertion_sorting(test_array)
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()