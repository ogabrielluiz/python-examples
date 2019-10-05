import unittest
from main import DecimalToOctal
from convertBetweenBases import *
 
# class TestDecimalToOctal(unittest.TestCase):

#     def test_success(self):
#         self.assertEquals(DecimalToOctal(10),'12') #success 

#     def test_failed(self):
#         self.assertEquals(DecimalToOctal(10),'14') #fail

class TestConvertToDecimal(unittest.TestCase):

	def test_convert_binary_to_decimal(self):
		self.assertEqual(ConvertToDecimal(1001, 2), 9)

	def test_convert_5_ary_to_decimal_success_2(self):
		self.assertEqual(ConvertToDecimal(2341, 5), 346)

	def test_convert_16_ary_to_decimal_success_2(self):
		self.assertEqual(ConvertToDecimal(125, 16), 293)

class TestConvertToDifferentBases(unittest.TestCase):

    def test_convert_to_different_bases_1(self):
        self.assertEqual(ConvertToDifferentBases(521, 13, 7), 2354) #success 

    def test_convert_to_different_bases_2(self):
        self.assertEqual(ConvertToDifferentBases(125, 16, 6 ), 1205) #success

    def test_convert_to_same_base(self):
        self.assertEqual(ConvertToDifferentBases(6, 35, 35 ), 6) #success

    def test_convert_from_binary(self):
        self.assertEqual(ConvertToDifferentBases(1011, 2, 6 ), 15) #success

if __name__ == '__main__':
    unittest.main()