import unittest
from fibonacciDynamicProgramming import fibonacciDP
 
class TestFibonacciDP(unittest.TestCase):

	def test_compute_1st_Fibonacci(self):
		self.assertEqual(fibonacciDP(1), 1)

	def test_compute_2nd_Fibonacci(self):
		self.assertEqual(fibonacciDP(2), 1)

	def test_compute_Fibonacci(self):
		self.assertEqual(fibonacciDP(100), 354224848179261915075)

if __name__ == '__main__':
    unittest.main()