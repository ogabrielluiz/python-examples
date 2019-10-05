import unittest
from main import BubleSort

class TestBubleSort(unittest.TestCase):

    def test_success(self):
        self.assertEqual(BubleSort([12, 3, 1, 7]), [1, 3, 7, 12]) #success

    def test_failed(self):
        self.assertEqual(BubleSort([12, 3, 1, 7]), [1, 3, 7, 13]) #failed

if __name__ == '__main__':
    unittest.main()
