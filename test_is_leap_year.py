import unittest
from my_packege.lesson_1 import is_leap_year


class TestLeapYear(unittest.TestCase):
    def test_leap_year(self):
        year = 2000
        res = is_leap_year(year)
        self.assertTrue(res)

    def test_zero_year(self):
        year = 0
        res = is_leap_year(year)
        self.assertFalse(res)


if __name__ == "__main__":
    unittest.main()
