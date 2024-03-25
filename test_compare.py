import unittest
from compare import convert_mixed_fraction, convert_mixed_fraction_in_expression


class TestConversionFunctions(unittest.TestCase):
    def test_convert_mixed_fraction(self):
        self.assertEqual(convert_mixed_fraction("1’1/2"), "(1 + 1/2)")
        self.assertEqual(convert_mixed_fraction("2"), "2")

    def test_convert_mixed_fraction_in_expression(self):
        self.assertEqual(convert_mixed_fraction_in_expression("1’1/2 + 2"), "(1 + 1/2) + 2")
        self.assertEqual(convert_mixed_fraction_in_expression("2 - 1’1/2"), "2 - (1 + 1/2)")


if __name__ == '__main__':
    unittest.main()
