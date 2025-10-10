import unittest

def multiply( x, y):
    return x * y


class TestMultiplyFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiply(3, 5), 15)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, 4), -8)

    def test_zero(self):
        self.assertEqual(multiply(0, 10), 0)


if __name__ == "__main__":
    unittest.main()