import my_lib
import unittest

class Test(unittest.TestCase):
    def test_multiply_3_4(self):
        self.assertEqual(my_lib.multiply(3, 4), 12)

    def test_multiply_3_a(self):
        self.assertEqual(my_lib.multiply(3, "a"), "aaa")

unittest.main()