import unittest

from filter_utils import strip_to_none


class FilterUtilsTest(unittest.TestCase):
    def test_strip_to_none_01(self):
        self.assertIsNone(strip_to_none(" "))

    def test_strip_to_none_02(self):
        self.assertEqual(strip_to_none(" blah "), "blah")


if __name__ == "__main__":
    unittest.main()
